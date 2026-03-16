import math


def simplify(a, b):
    dzielnik = math.gcd(a,b)
    x = a/dzielnik
    y = b/dzielnik
    return x,y