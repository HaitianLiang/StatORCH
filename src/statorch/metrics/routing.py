def oracle_headroom_capture(fallback,selected,oracle,direction='down'):
    if direction=='down': num=fallback-selected; den=fallback-oracle
    else: num=selected-fallback; den=oracle-fallback
    return float(num/den) if abs(den)>1e-12 else 0.0
