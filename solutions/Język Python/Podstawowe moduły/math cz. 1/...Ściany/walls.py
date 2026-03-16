import math


def walls(x):
    if x > 0:
        return math.floor(x)
    else:
        return math.ceil(x)