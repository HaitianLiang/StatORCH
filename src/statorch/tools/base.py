from __future__ import annotations
from dataclasses import dataclass, field
from typing import Callable, Any

@dataclass
class ToolResult:
    name: str
    outputs: dict[str, Any]
    cost: float = 0.0
    warnings: list[str] = field(default_factory=list)
    converged: bool = True

@dataclass
class Tool:
    name: str
    run_fn: Callable[..., ToolResult]
    def run(self, *args, **kwargs): return self.run_fn(*args, **kwargs)
