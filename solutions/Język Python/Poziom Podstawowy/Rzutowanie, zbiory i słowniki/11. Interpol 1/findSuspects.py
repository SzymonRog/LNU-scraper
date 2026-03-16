def findSuspects(x, y, z):
    return ( set(x) & set(y) ) | ( set(x) & set(z) ) | (set(y) & set(z) )