def optimize( operations, toRemove ):
    przesunięcie = 0
    for x in toRemove:
        del(operations[x - przesunięcie])
        przesunięcie += 1
        
    return operations