from statorch.agent.state import StatisticalState

def refresh_state(previous: StatisticalState, **updates) -> StatisticalState:
    data=previous.to_dict()
    for key,value in updates.items():
        if key not in data: raise KeyError(f"Unknown state field: {key}")
        data[key]=value
    return StatisticalState(**data)
