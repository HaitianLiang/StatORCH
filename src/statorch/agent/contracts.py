from __future__ import annotations
from dataclasses import dataclass, field
from typing import Callable, Any

@dataclass
class ToolContract:
    name: str
    family: str
    requirements: tuple[str,...] = ()
    precondition: Callable[[Any], bool] = lambda state: True
    outputs: tuple[str,...] = ()
    target_diagnostics: dict[str,int] = field(default_factory=dict)  # +1 higher is better, -1 lower
    cost: float = 0.0
    failure_modes: tuple[str,...] = ()
    def is_valid(self,state,remaining_cost=float('inf')):
        return self.cost <= remaining_cost and bool(self.precondition(state))
