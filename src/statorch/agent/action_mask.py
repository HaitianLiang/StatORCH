def valid_actions(contracts,state,remaining_cost=float('inf')):
    return [name for name,c in contracts.items() if c.is_valid(state,remaining_cost)]
