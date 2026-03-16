import math


def filtered_sqrt(x):
    try:
        return math.sqrt(x)
    except:
        return "Funkcja sqrt() nie obsługuje liczb zespolonych"