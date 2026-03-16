import math


def elementwise_mult(lists):
    dlugosc = len(lists[0])
    liczby = [1 for i in lists[0]]
    for i in lists:
        for j in range(dlugosc):
            liczby[j] *= i[j]
    return liczby
        
        
        
        
        
        
