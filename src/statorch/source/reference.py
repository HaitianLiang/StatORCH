from __future__ import annotations
from dataclasses import dataclass
import numpy as np

@dataclass
class GaussianReference:
    means: np.ndarray
    cov_inv: np.ndarray


def fit_gaussian_reference(x: np.ndarray, y: np.ndarray, ridge: float = 1e-3) -> GaussianReference:
    classes=np.unique(y)
    means=[]; covs=[]
    for k in classes:
        z=x[y==k]
        means.append(z.mean(axis=0))
        c=np.cov(z,rowvar=False)
        if np.ndim(c)==0: c=np.array([[float(c)]])
        c=c+ridge*np.eye(c.shape[0])
        covs.append(np.linalg.pinv(c))
    return GaussianReference(np.asarray(means), np.asarray(covs))
