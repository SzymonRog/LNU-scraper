import math

def calculate_error(x):
    n1 = math.exp(x) - 1
    n2 = math.expm1(x)
    return (n1 - n2 )/ n2
    