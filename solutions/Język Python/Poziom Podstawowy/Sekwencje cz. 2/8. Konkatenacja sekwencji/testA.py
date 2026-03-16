def testA( t1, t2 ):
    if t1.count('a') > t2.count('a') or t1.count('a') == t2.count('a'):
        c = t1 + t2
    else:
        c= t2 + t1
    
    return c