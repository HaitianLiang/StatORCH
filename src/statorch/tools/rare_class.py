def rare_status(low, high, detect_threshold=0.0, rare_threshold=0.02):
    if not 0 <= detect_threshold < rare_threshold:
        raise ValueError('Require 0 <= detect_threshold < rare_threshold')
    if low > rare_threshold: return 'present/non-rare'
    if low > detect_threshold and high <= rare_threshold: return 'rare-present'
    if high <= detect_threshold: return 'below-reporting-threshold'
    return 'unresolved'
