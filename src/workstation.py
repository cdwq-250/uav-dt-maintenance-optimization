from dataclasses import dataclass

from src.equipment import Equipment


@dataclass
class Workstation:
    station_id: str
    station_type: str
    equipment: Equipment
    available_time: float = 0.0

    def earliest_start(self) -> float:
        return max(self.available_time, self.equipment.busy_until)
