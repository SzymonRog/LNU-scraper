import numpy as np

def fillSquare(length):
    idx = np.arange(length)
    row_dist = np.minimum(idx, length - 1 - idx)
    col_dist = np.minimum(idx, length - 1 - idx)

    return np.minimum.outer(row_dist, col_dist)
