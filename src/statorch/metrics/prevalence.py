import numpy as np

def project_simplex(v: np.ndarray) -> np.ndarray:
    v=np.asarray(v,float)
    if v.ndim != 1: raise ValueError('project_simplex expects 1-D')
    u=np.sort(v)[::-1]; cssv=np.cumsum(u)-1
    ind=np.arange(1,len(v)+1); cond=u-cssv/ind>0
    rho=ind[cond][-1] if cond.any() else 1
    theta=cssv[rho-1]/rho
    w=np.maximum(v-theta,0)
    return w/w.sum() if w.sum()>0 else np.full_like(w,1/len(w))

def l1_error(est, truth): return float(np.abs(np.asarray(est)-np.asarray(truth)).sum())

def entropy(p, eps=1e-12):
    p=np.clip(np.asarray(p,float),eps,1); return float(-(p*np.log(p)).sum())
