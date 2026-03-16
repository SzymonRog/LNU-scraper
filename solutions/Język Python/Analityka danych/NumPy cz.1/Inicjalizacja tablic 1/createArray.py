import numpy as np

def createArray(a, b, c):
    return np.full((a, b), str(c), dtype='<U4')
