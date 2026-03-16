def countGarfield( names ):
    n = 1
    while 1: 
        l = next(names)
        if l == "Garfield":
            return n
        else:
            n += 1 
        