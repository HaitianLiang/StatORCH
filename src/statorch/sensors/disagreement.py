import numpy as np

def estimator_disagreement(estimates):
    arr=np.asarray(estimates,float)
    if len(arr)<2: return 0.0
    return float(max(np.abs(arr[i]-arr[j]).sum() for i in range(len(arr)) for j in range(i)))
