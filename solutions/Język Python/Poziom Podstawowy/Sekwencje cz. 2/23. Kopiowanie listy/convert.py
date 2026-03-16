def convert( x ):
    y = list(x)
    for i in range(len(y)):
        if y[i] < 0:
            y[i] = 0
        elif y[i] > 10:
            y[i] = 10
        else:
            y[i] = x[i]
            
    z = x + y
    return  z
    
    
