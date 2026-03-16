import numpy as np

def checkData(results):
    nan_count = np.isnan(results).sum()
    total_count = results.size
    return nan_count / total_count < 0.3
