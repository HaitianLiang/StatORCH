from dataclasses import dataclass, asdict
@dataclass
class ToolHealth:
    converged: bool = True
    runtime_s: float = 0.0
    warnings: tuple[str,...] = ()
    def to_dict(self): return asdict(self)
