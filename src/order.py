from dataclasses import dataclass, field


@dataclass(frozen=True)
class ProcessStep:
    name: str
    workstation_type: str
    processing_time: float


@dataclass
class Order:
    order_id: str
    due_date: float
    priority: int
    route: list[ProcessStep]
    current_step_index: int = 0
    ready_time: float = 0.0
    completion_time: float | None = None
    history: list[dict] = field(default_factory=list)

    @property
    def is_complete(self) -> bool:
        return self.current_step_index >= len(self.route)

    @property
    def current_step(self) -> ProcessStep | None:
        if self.is_complete:
            return None
        return self.route[self.current_step_index]

    def advance(self, finish_time: float) -> None:
        self.current_step_index += 1
        self.ready_time = finish_time
        if self.is_complete:
            self.completion_time = finish_time
