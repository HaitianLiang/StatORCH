import numpy as np

def prediction_entropy(proba, eps=1e-12):
    p=np.clip(np.asarray(proba,float),eps,1)
    return float((-(p*np.log(p)).sum(axis=1)).mean())

def prediction_stability(p_before,p_after):
    a=np.asarray(p_before,float); b=np.asarray(p_after,float)
    return float(1.0-np.abs(a-b).mean())
