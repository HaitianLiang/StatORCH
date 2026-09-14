from __future__ import annotations
from typing import Mapping

def verify_diagnostics(before: Mapping[str,float], after: Mapping[str,float], targets: Mapping[str,int], tol=1e-8):
    deltas={}; supported=[]
    for key,orient in targets.items():
        if key not in before or key not in after: continue
        d=orient*(after[key]-before[key]); deltas[key]=float(d); supported.append(d>tol)
    if not supported: status='inconclusive'
    elif all(supported): status='diagnostic-supported'
    else: status='diagnostic-unsupported'
    return {'status':status,'oriented_deltas':deltas}
