import numpy as np

def createArray(shape):
    rows, cols = shape
    total = rows * cols
    
    arr = np.zeros(total, dtype=int)
    
    # indeksy co drugiego elementu
    indexes = np.arange(0, total, 2)
    
    # kolejne liczby naturalne
    values = np.arange(1, len(indexes) + 1)
    
    # wstawiamy wartości
    np.put(arr, indexes, values)
    
    return arr.reshape(shape)