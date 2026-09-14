from __future__ import annotations
import numpy as np

def random_policy(valid_actions, rng=None):
    rng=np.random.default_rng() if rng is None else rng
    return valid_actions[int(rng.integers(len(valid_actions)))]

def best_gain_per_cost(gains: dict[str,float], costs: dict[str,float], valid_actions=None):
    actions=valid_actions or list(gains)
    return max(actions,key=lambda a:gains[a]/max(costs[a],1e-12))

def health_aware_bundle(discrepancy: dict[str,float], uncertainty: dict[str,float], costs: dict[str,float]):
    """Transparent demo policy: favor low-discrepancy, high-uncertainty-reduction bundles."""
    scores={a:(uncertainty.get(a,0.0)+1e-6)/(1.0+discrepancy.get(a,0.0))/max(costs[a],1e-9) for a in costs}
    return max(scores,key=scores.get), scores


def select_groups_under_budget(scores: dict[str,float], costs: dict[str,float], budget: float):
    """Greedy group selection by score/cost. Useful for fixed/static AFA baselines."""
    ordered=sorted(scores,key=lambda a:(scores[a]/max(costs[a],1e-12),scores[a]),reverse=True)
    chosen=[]; spent=0.0
    for a in ordered:
        c=float(costs[a])
        if spent+c<=budget+1e-12:
            chosen.append(a); spent+=c
    return chosen,spent

def static_afa(calibration_utility: dict[str,float], costs: dict[str,float], budget: float):
    return select_groups_under_budget(calibration_utility,costs,budget)

def myopic_afa(expected_uncertainty_reduction: dict[str,float], costs: dict[str,float], budget: float):
    return select_groups_under_budget(expected_uncertainty_reduction,costs,budget)

def gsm_afa(available: list[str], costs: dict[str,float], budget: float, monte_carlo_utility):
    """Generic generative-surrogate AFA interface.

    `monte_carlo_utility(group)` must evaluate expected post-acquisition utility from a
    fitted domain-specific surrogate. StatOrch deliberately leaves the surrogate
    model to the dataset adapter instead of inventing one generic density model.
    """
    scores={a:float(monte_carlo_utility(a)) for a in available}
    return select_groups_under_budget(scores,costs,budget)
