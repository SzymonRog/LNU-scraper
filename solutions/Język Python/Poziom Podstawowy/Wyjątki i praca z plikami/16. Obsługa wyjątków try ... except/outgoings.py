def outgoings(x):
    s = 0
    for i in x:
        try:
            if i < 0:
                s += float(i)
        except:
            pass
    return s