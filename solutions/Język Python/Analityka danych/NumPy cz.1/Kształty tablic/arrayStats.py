import numpy as np

def arrayStats(arr):
    shape = arr.shape
    
    size = 1
    for dim in shape:
        size *= dim

    return len(shape), size, shape
