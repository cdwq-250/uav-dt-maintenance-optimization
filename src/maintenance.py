from dataclasses import dataclass
from typing import Literal

from src.config import SimulationConfig
from src.equipment import Equipment

MaintenancePolicyName = Literal["corrective", "preventive", "condition_based"]


@dataclass(frozen=True)
class MaintenanceDecision:
    required: bool
    duration: float = 0.0
    reason: str = "none"


class MaintenancePolicy:
    def __init__(self, name: MaintenancePolicyName) -> None:
        self.name = name

    def decide_before_processing(
        self,
        equipment: Equipment,
        config: SimulationConfig,
    ) -> MaintenanceDecision:
        if equipment.needs_corrective_maintenance(config):
            return MaintenanceDecision(
                True,
                config.corrective_maintenance_time,
                "corrective",
            )

        if self.name in {"preventive", "condition_based"} and equipment.needs_preventive_maintenance(config):
            return MaintenanceDecision(
                True,
                config.preventive_maintenance_time,
                self.name,
            )

        return MaintenanceDecision(False)
