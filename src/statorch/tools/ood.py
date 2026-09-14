from __future__ import annotations
import numpy as np
from statorch.source.reference import GaussianReference

def mahalanobis_score(x: np.ndarray, ref: GaussianReference) -> np.ndarray:
    vals=[]
    for mean,inv in zip(ref.means,ref.cov_inv):
        d=x-mean
        vals.append(np.einsum('ni,ij,nj->n',d,inv,d))
    # Larger = more out-of-reference.
    return np.min(np.stack(vals,axis=1),axis=1)
