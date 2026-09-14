from __future__ import annotations
import numpy as np
from statorch.metrics.prevalence import project_simplex


def pcc(target_proba: np.ndarray) -> np.ndarray:
    q=np.asarray(target_proba,float).mean(axis=0)
    return project_simplex(q)


def emq(target_proba: np.ndarray, source_prior: np.ndarray, max_iter: int = 500,
        tol: float = 1e-9) -> np.ndarray:
    """Saerens/SLD-style EM prior adjustment from calibrated source posteriors."""
    p=np.clip(np.asarray(target_proba,float),1e-12,1.0)
    pi=np.clip(np.asarray(source_prior,float),1e-12,None); pi=pi/pi.sum()
    q=pi.copy()
    for _ in range(max_iter):
        w=p*(q/pi)[None,:]
        w=w/np.clip(w.sum(axis=1,keepdims=True),1e-12,None)
        q_new=w.mean(axis=0); q_new=project_simplex(q_new)
        if np.abs(q_new-q).sum()<tol: q=q_new; break
        q=q_new
    return q


def pacc(target_proba: np.ndarray, source_proba: np.ndarray, source_y: np.ndarray,
         ridge: float = 1e-5) -> np.ndarray:
    classes=np.arange(target_proba.shape[1])
    C=np.column_stack([source_proba[source_y==k].mean(axis=0) for k in classes])
    b=target_proba.mean(axis=0)
    q=np.linalg.solve(C.T@C+ridge*np.eye(len(classes)), C.T@b)
    return project_simplex(q)


def bbse(target_pred: np.ndarray, source_pred: np.ndarray, source_y: np.ndarray,
         ridge: float = 1e-5) -> np.ndarray:
    K=int(max(source_y.max(),source_pred.max(),target_pred.max())+1)
    C=np.zeros((K,K))
    for k in range(K):
        z=source_pred[source_y==k]
        for j in range(K): C[j,k]=(z==j).mean() if len(z) else 0
    b=np.bincount(target_pred,minlength=K)/len(target_pred)
    q=np.linalg.solve(C.T@C+ridge*np.eye(K), C.T@b)
    return project_simplex(q)
