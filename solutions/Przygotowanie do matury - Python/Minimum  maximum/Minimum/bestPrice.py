import math
def bestPrice( prices ):
    minimum = math.inf
    for i in prices:
        if i < minimum:
            minimum = i
    return minimum