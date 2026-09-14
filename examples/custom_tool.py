from statorch.agent.contracts import ToolContract
from statorch.agent.state import StatisticalState

contract=ToolContract(
    name='MY_TOOL', family='custom', cost=1.0,
    precondition=lambda s: s.cost.get('remaining',0)>=1,
    outputs=('my_statistic',), target_diagnostics={'uncertainty':-1},
)
state=StatisticalState(cost={'remaining':3})
print('valid:',contract.is_valid(state,state.cost['remaining']))
