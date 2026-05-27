from dataclasses import dataclass

from src.config import SimulationConfig
from src.equipment import Equipment
from src.maintenance import MaintenancePolicy, MaintenancePolicyName
from src.order import Order
from src.process import default_uav_route, short_repair_route
from src.scheduler import DispatchRule, Scheduler
from src.workstation import Workstation


@dataclass
class SimulationResult:
    orders: list[Order]
    workstations: list[Workstation]
    event_log: list[dict]
    policy_name: str
    dispatch_rule: str


class Simulation:
    def __init__(
        self,
        config: SimulationConfig,
        orders: list[Order],
        workstations: list[Workstation],
        dispatch_rule: DispatchRule = "edd",
        maintenance_policy: MaintenancePolicyName = "condition_based",
    ) -> None:
        self.config = config
        self.orders = orders
        self.workstations = workstations
        self.scheduler = Scheduler(dispatch_rule)
        self.maintenance_policy = MaintenancePolicy(maintenance_policy)
        self.event_log: list[dict] = []

    def run(self) -> SimulationResult:
        while not all(order.is_complete for order in self.orders):
            progressed = False

            for station in sorted(self.workstations, key=lambda item: item.earliest_start()):
                order = self.scheduler.select_order(self.orders, station)
                if order is None or order.current_step is None:
                    continue

                start_time = max(station.earliest_start(), order.ready_time)
                decision = self.maintenance_policy.decide_before_processing(
                    station.equipment,
                    self.config,
                )
                if decision.required:
                    finish_time = station.equipment.maintain(
                        start_time,
                        decision.duration,
                        self.config,
                    )
                    station.available_time = finish_time
                    self.event_log.append(
                        {
                            "event": "maintenance",
                            "station_id": station.station_id,
                            "equipment_id": station.equipment.equipment_id,
                            "start": start_time,
                            "finish": finish_time,
                            "reason": decision.reason,
                        }
                    )
                    start_time = finish_time

                step = order.current_step
                finish_time = start_time + step.processing_time
                station.available_time = finish_time
                station.equipment.busy_until = finish_time
                station.equipment.degrade(step.processing_time, self.config)

                order.history.append(
                    {
                        "station_id": station.station_id,
                        "process": step.name,
                        "start": start_time,
                        "finish": finish_time,
                    }
                )
                order.advance(finish_time)
                self.event_log.append(
                    {
                        "event": "process",
                        "order_id": order.order_id,
                        "station_id": station.station_id,
                        "process": step.name,
                        "start": start_time,
                        "finish": finish_time,
                    }
                )
                progressed = True

            if not progressed:
                raise RuntimeError("Simulation stalled because no station can process remaining orders.")

        return SimulationResult(
            orders=self.orders,
            workstations=self.workstations,
            event_log=self.event_log,
            policy_name=self.maintenance_policy.name,
            dispatch_rule=self.scheduler.rule,
        )


def build_default_simulation(
    config: SimulationConfig,
    dispatch_rule: DispatchRule = "edd",
    maintenance_policy: MaintenancePolicyName = "condition_based",
) -> Simulation:
    orders = [
        Order("UAV-001", due_date=22.0, priority=2, route=default_uav_route()),
        Order("UAV-002", due_date=18.0, priority=3, route=short_repair_route()),
        Order("UAV-003", due_date=28.0, priority=1, route=default_uav_route()),
    ]
    workstations = [
        Workstation("A1", "assembly", Equipment("EQ-A1", config.initial_health)),
        Workstation("E1", "electronics", Equipment("EQ-E1", config.initial_health)),
        Workstation("T1", "testing", Equipment("EQ-T1", config.initial_health)),
        Workstation("I1", "inspection", Equipment("EQ-I1", config.initial_health)),
    ]
    return Simulation(config, orders, workstations, dispatch_rule, maintenance_policy)
