import numpy as np

def repair(table):
    n = table.shape[0]
    
    # Posortuj każdy rząd
    for i in range(n):
        table[i] = np.sort(table[i])
    
    # Posortuj rzędy po pierwszym elemencie (czyli po "której to tabliczki")
    table[:] = table[np.argsort(table[:, 0])]
    
    return table