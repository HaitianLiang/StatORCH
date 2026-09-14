import numpy as np
from statorch.tools.quantification import pcc, emq, pacc

def test_quantifiers_simplex():
    p=np.array([[.8,.2],[.7,.3],[.2,.8],[.1,.9]])
    prior=np.array([.5,.5])
    for q in [pcc(p),emq(p,prior)]:
        assert np.all(q>=0) and np.isclose(q.sum(),1)

def test_emq_fixed_when_matching_prior():
    p=np.tile(np.array([[.5,.5]]),(20,1))
    q=emq(p,np.array([.5,.5])); assert np.allclose(q,[.5,.5],atol=1e-7)
