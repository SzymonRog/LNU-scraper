def hasNotAnanym(x):
    y = list(x)
    for i in x:
        if i[::-1] in x:
            y.remove(i)
           
    return y
   
   