import math


def modulus_fractional_ratio(x):
    n, całosc = math.modf(x)
    liczba = 0.0
    razy = 0
    if n == 0:
        return -1
    elif całosc > 0:
        while not liczba >= całosc:
            liczba += n
            razy += 1
    else:
        while not liczba <= całosc:
            liczba += n
            razy += 1
    return razy
            