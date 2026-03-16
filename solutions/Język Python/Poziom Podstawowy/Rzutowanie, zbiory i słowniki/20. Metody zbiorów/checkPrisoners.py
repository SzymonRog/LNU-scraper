def checkPrisoners( t, i ):
    x = set(t.items())
    y = set(i.items())
    if x.issubset(y) or y.issubset(x):
        return True
    return False
    
                
