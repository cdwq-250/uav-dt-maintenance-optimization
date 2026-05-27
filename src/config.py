from dataclasses import dataclass


@dataclass(frozen=True)
class SimulationConfig:
    random_seed: int = 42
    degradation_per_hour: float = 0.04
    failure_threshold: float = 0.2
    maintenance_threshold: float = 0.35
    corrective_maintenance_time: float = 6.0
    preventive_maintenance_time: float = 3.0
    initial_health: float = 1.0
    maintenance_cost_per_hour: float = 120.0
    tardiness_cost_per_hour: float = 80.0
