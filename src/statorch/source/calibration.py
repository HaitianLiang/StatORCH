from __future__ import annotations
import numpy as np

def clip_and_normalize(p: np.ndarray, eps: float = 1e-9) -> np.ndarray:
    p=np.clip(np.asarray(p,float),eps,None)
    return p/p.sum(axis=1,keepdims=True)
