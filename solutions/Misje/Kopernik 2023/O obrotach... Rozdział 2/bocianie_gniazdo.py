import math

def widocznosc(R, h):
    zasieg = math. floor((math.sqrt(((h + R) ** 2) - R**2)))
    return zasieg