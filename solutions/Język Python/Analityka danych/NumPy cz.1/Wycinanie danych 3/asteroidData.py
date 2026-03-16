import numpy as np

def get_asteroid_data(data, asteroid_indices, time_indices, data_type):
    data_indices = {"P": [0, 1, 2], "V": [3], "R": [4]}
    
    result = np.take(data, asteroid_indices, axis=0)
    result = np.take(result, time_indices, axis=1)
    result = np.take(result, data_indices[data_type], axis=2)
    
    return result