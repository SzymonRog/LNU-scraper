import math, balloons

def calcVolume():
    V = 0.0
    for x in range(balloons.balloonsNumber()):
        R = balloons.getRadius(x) / 10
        V += 4/3 * math.pi * R ** 3
    return V