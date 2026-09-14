from __future__ import annotations
from dataclasses import dataclass, field, asdict
from typing import Any

@dataclass
class DecisionCertificate:
    step: int
    evidence: dict[str, Any]
    diagnosis: dict[str, float]
    action: dict[str, Any]
    verification: dict[str, Any]
    status: str
    note: str = 'Auditability record; not a correctness guarantee.'
    def to_dict(self): return asdict(self)
