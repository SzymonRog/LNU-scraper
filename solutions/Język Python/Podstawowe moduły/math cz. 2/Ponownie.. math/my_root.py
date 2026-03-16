import math

def my_root(number, degree):
    answere = 0
    if degree == 2:
        answere = math.sqrt(number)
    elif degree == 3:
        answere = math.cbrt(number)
    elif degree > 3 :
        answere = math.pow(number, 1/degree)
    return answere