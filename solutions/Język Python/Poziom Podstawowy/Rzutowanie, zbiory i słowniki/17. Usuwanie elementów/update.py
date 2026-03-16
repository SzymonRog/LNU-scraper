import time
def update(x):
    t = 20190709
    y = dict(x)
    for i in x:
        if int(x[i][1]) < t:
            del y[i]
    return y 
        