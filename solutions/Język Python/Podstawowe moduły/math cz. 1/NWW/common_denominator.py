import math


def common_denominator(a, b):
    z = math.lcm(a,b)
    y = int(z/b)
    x = int(z/a)
    return (x,y,z)
    
    