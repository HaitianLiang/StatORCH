import numpy as np
from statorch.sensors.shift import mmd_rbf
from statorch.sensors.uncertainty import bootstrap_emq

def test_mmd_identity_small():
    rng=np.random.default_rng(0); x=rng.normal(size=(80,3))
    assert mmd_rbf(x,x) < 1e-8

def test_bootstrap_shape():
    p=np.tile([[.7,.3]],(40,1)); r=bootstrap_emq(p,np.array([.5,.5]),reps=10)
    assert len(r['low'])==2 and r['mean_width']>=0
