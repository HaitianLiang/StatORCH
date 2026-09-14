from statorch.agent.state import StatisticalState
from statorch.agent.contracts import ToolContract
from statorch.agent.verifier import verify_diagnostics

def test_contract_cost_gate():
    s=StatisticalState(cost={'remaining':2})
    c=ToolContract('x','test',cost=3)
    assert not c.is_valid(s,2)

def test_verifier_orientation():
    v=verify_diagnostics({'unc':.2,'fit':.5},{'unc':.1,'fit':.7},{'unc':-1,'fit':1})
    assert v['status']=='diagnostic-supported'
