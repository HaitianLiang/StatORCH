from __future__ import annotations
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import StratifiedKFold, cross_val_predict
from sklearn.metrics import roc_auc_score


def _rbf_gamma(x,y):
    z=np.vstack([x,y]); n=min(len(z),400); z=z[:n]
    d=((z[:,None,:]-z[None,:,:])**2).sum(-1)
    vals=d[np.triu_indices_from(d,1)]; med=np.median(vals[vals>0]) if np.any(vals>0) else 1.0
    return 1.0/max(med,1e-12)

def mmd_rbf(x,y,gamma=None):
    x=np.asarray(x,float); y=np.asarray(y,float); gamma=_rbf_gamma(x,y) if gamma is None else gamma
    kxx=np.exp(-gamma*((x[:,None,:]-x[None,:,:])**2).sum(-1))
    kyy=np.exp(-gamma*((y[:,None,:]-y[None,:,:])**2).sum(-1))
    kxy=np.exp(-gamma*((x[:,None,:]-y[None,:,:])**2).sum(-1))
    return float(max(kxx.mean()+kyy.mean()-2*kxy.mean(),0.0))

def domain_classifier_auc(x_source,x_target,seed=0):
    xs=np.asarray(x_source); xt=np.asarray(x_target)
    # cap for speed / balance
    n=min(len(xs),len(xt),800); xs=xs[:n]; xt=xt[:n]
    X=np.vstack([xs,xt]); y=np.concatenate([np.zeros(n),np.ones(n)])
    cv=StratifiedKFold(n_splits=3,shuffle=True,random_state=seed)
    pred=cross_val_predict(LogisticRegression(max_iter=400),X,y,cv=cv,method='predict_proba')[:,1]
    return float(roc_auc_score(y,pred))
