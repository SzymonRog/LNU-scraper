def brutto( x ):
    y = x.split()

    return str(round(float(y[0]) * 1.08, 2)) + " "+  y[1]