import numpy as np

def known_support_summary(proba):
    p=np.asarray(proba,float); m=p.max(axis=1)
    return {'mean_max_p':float(m.mean()),'low_support_fraction':float((m<0.5).mean())}
