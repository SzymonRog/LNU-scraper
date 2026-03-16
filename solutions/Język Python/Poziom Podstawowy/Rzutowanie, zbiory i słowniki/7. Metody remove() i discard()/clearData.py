def clearData( x, y ):
    z = set(x)
    for i in x:
        if i[1] > y:
            z.discard(i)
            
    return z