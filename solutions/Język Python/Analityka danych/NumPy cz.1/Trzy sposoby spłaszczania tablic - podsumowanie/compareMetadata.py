import numpy as np

def flatten_metadata(arrays):
    ravel_list = []
    flatten_list = []
    flat_list = []

    for arr in arrays:
        
        ravel_list.append(arr.ravel())
        flatten_list.append(arr.flatten())
        flat_list.append(np.array(list(arr.flat)))

    return ravel_list, flatten_list, flat_list
