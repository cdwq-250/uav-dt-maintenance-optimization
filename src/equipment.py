from dataclasses import dataclass

from src.config import SimulationConfig


@dataclass
class Equipment:
    equipment_id: str
    health: float
    busy_until: float = 0.0
    maintenance_count: int = 0
    maintenance_downtime: float = 0.0

    def degrade(self, processing_time: float, config: SimulationConfig) -> None:
        self.health = max(0.0, self.health - processing_time * config.degradation_per_hour)

    def needs_corrective_maintenance(self, config: SimulationConfig) -> bool:
        return self.health <= config.failure_threshold

    def needs_preventive_maintenance(self, config: SimulationConfig) -> bool:
        return self.health <= config.maintenance_threshold

    def maintain(self, start_time: float, duration: float, config: SimulationConfig) -> float:
        finish_time = start_time + duration
        self.busy_until = finish_time
        self.health = config.initial_health
        self.maintenance_count += 1
        self.maintenance_downtime += duration
        return finish_time
