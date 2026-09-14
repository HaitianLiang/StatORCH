from __future__ import annotations
from dataclasses import dataclass, field, asdict
from typing import Any

@dataclass
class StatisticalState:
    population: dict[str, Any] = field(default_factory=dict)
    uncertainty: dict[str, Any] = field(default_factory=dict)
    discrepancy: dict[str, Any] = field(default_factory=dict)
    fit: dict[str, Any] = field(default_factory=dict)
    representation: dict[str, Any] = field(default_factory=dict)
    open_world: dict[str, Any] = field(default_factory=dict)
    information: dict[str, Any] = field(default_factory=dict)
    cost: dict[str, Any] = field(default_factory=dict)
    tool_health: dict[str, Any] = field(default_factory=dict)
    history: list[dict[str, Any]] = field(default_factory=list)
    data_version: int = 0
    representation_version: int = 0
    def to_dict(self): return asdict(self)
