import numpy as np
from primeFactors import primeFactors  # zakładamy, że funkcja istnieje

def reshapeArray(arr):
    # liczba elementów w tablicy
    n = arr.size
    
    # pobierz czynniki pierwsze liczby elementów
    factors = primeFactors(n)
    
    # przekształć tablicę w nowy kształt
    reshaped = arr.reshape(factors)
    
    return reshaped
