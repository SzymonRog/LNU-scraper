import numpy as np

def distributePower(battery1, battery2, threshold):
    battery1 = np.array(battery1)
    battery2 = np.array(battery2)
    
    valid1 = battery1 >= threshold
    valid2 = battery2 >= threshold
    
    choose1 = valid1 & ((battery1 >= battery2) | (~valid2))
    choose2 = valid2 & (battery2 > battery1)
    
    return np.where(choose1, 1,
           np.where(choose2, 2, 0))