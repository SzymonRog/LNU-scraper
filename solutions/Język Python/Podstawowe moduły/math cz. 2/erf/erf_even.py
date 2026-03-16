import math

def erf_even(scope, points):
    step = 2 * scope / (points - 1)  
    coordinates = []
    
    for i in range(points):
        x = -scope + i * step 
        coordinates.append([x, math.erf(x)])  
    return coordinates