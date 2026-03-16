def getFeatures( x ):
    z = set(x[0])
    for i in x:
        z &= set(i)
            
            
    return z
