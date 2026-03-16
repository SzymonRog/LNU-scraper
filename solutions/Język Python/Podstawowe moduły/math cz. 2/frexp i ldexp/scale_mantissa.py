import math 

def scale_mantissa(number,scale):
    man,wyk = math.frexp(number)
    n = scale/100
    return math.ldexp(man * n,wyk)
    
    