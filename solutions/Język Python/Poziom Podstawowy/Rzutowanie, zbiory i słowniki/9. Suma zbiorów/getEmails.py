def getEmails( s1, s2 ):
    y = set()
    z = set()
    
    for i in s1:
        if i[1] == True:
            y.add(i[0])
    for i in s2:
        if i[1] == True:
            z.add(i[0])
    w =  y.union(z)
    
    return w