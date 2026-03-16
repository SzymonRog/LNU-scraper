def findLongest(x):
    m = x[0]
    for i in x:
        if len(m) < len(i):
            m = i
    return m