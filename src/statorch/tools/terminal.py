def resolved(fit_score, uncertainty_width, stability_l1, *, min_fit=.5, max_uncertainty=.1, max_stability=.03):
    return bool(fit_score>=min_fit and uncertainty_width<=max_uncertainty and stability_l1<=max_stability)
