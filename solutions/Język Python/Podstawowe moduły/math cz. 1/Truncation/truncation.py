import math


def round_away_from_zero(n):
    if n == 0:
        return n
    elif n > 0:
        liczba = math.trunc(n) + 1
        return liczba
    else:
        liczba = math.trunc(n) - 1
        return liczba