import random


def noise(x, y):
    return [random.getrandbits(8) for i in range(x*y)]