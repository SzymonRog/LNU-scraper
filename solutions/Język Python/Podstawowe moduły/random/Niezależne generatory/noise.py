import random


def noise(x, y):
    
    los = random.Random()
    return [los.getrandbits(2) for i in range(x*y)]