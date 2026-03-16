import math
def bestValue( notes ):
    maximum = -math.inf
    for i in notes:
        if i > maximum:
            maximum = i
    return maximum