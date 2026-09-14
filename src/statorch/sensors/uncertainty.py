from __future__ import annotations
import numpy as np
from statorch.tools.quantification import emq

def bootstrap_emq(target_proba, source_prior, reps=200, seed=0, alpha=0.05):
    rng=np.random.default_rng(seed); n=len(target_proba); vals=[]
    for _ in range(reps):
        idx=rng.integers(0,n,size=n); vals.append(emq(target_proba[idx],source_prior))
    a=np.asarray(vals); lo=np.quantile(a,alpha/2,axis=0); hi=np.quantile(a,1-alpha/2,axis=0)
    return {'low':lo,'high':hi,'width':hi-lo,'mean_width':float((hi-lo).mean()),'max_width':float((hi-lo).max())}
