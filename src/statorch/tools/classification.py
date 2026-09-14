import numpy as np

def prior_correct(proba, source_prior, target_prior, eps=1e-12):
    p=np.clip(np.asarray(proba,float),eps,1)
    s=np.clip(np.asarray(source_prior,float),eps,None)
    t=np.clip(np.asarray(target_prior,float),eps,None)
    w=p*(t/s)[None,:]
    return w/np.clip(w.sum(axis=1,keepdims=True),eps,None)
