from __future__ import annotations
from dataclasses import dataclass, field
from .certificate import DecisionCertificate
from .verifier import verify_diagnostics

@dataclass
class ControllerLedger:
    certificates: list[DecisionCertificate] = field(default_factory=list)
    def append(self,c): self.certificates.append(c)
    def to_list(self): return [c.to_dict() for c in self.certificates]


def make_certificate(step,evidence,diagnosis,action,before,after,target_diagnostics):
    v=verify_diagnostics(before,after,target_diagnostics)
    return DecisionCertificate(step,evidence,diagnosis,action,v,v['status'])
