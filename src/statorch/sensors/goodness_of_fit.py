from __future__ import annotations
import numpy as np
from scipy.spatial.distance import jensenshannon

def posterior_residual(target_proba, beta):
    obs=np.asarray(target_proba).mean(axis=0); pred=np.asarray(beta,float)
    obs=obs/obs.sum(); pred=pred/pred.sum()
    return float(jensenshannon(obs,pred,base=2.0)**2)

def fit_score_from_residual(residual, scale=12.0):
    # Bounded descriptive fit score, not a p-value.
    return float(np.exp(-scale*max(residual,0.0)))
