from typing import Literal

from src.order import Order
from src.workstation import Workstation

DispatchRule = Literal["fifo", "edd", "spt"]


class Scheduler:
    def __init__(self, rule: DispatchRule = "edd") -> None:
        self.rule = rule

    def select_order(self, orders: list[Order], station: Workstation) -> Order | None:
        candidates = [
            order
            for order in orders
            if order.current_step is not None
            and order.current_step.workstation_type == station.station_type
        ]
        if not candidates:
            return None

        if self.rule == "fifo":
            return candidates[0]
        if self.rule == "spt":
            return min(candidates, key=lambda order: order.current_step.processing_time)
        return min(candidates, key=lambda order: (order.due_date, -order.priority))
