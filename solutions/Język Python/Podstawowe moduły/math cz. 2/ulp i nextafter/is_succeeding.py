import math

def is_succeeding(x):
    sucList=[]
    for i in range(1,len(x)-1):
        if x[i]==x[i-1]+math.ulp(x[i-1]) and x[i]==x[i+1]-math.ulp(x[i+1]):
            sucList.append(True)
        else:
            sucList.append(False)
    return sucList