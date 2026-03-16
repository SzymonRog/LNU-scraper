import math

def diameter(pixels: list[int]) -> float:
    count = 0 
    for i in pixels:
        count += (i == 16384000)
        
        
    count = count*0.25
    return math.sqrt(count/math.pi)*2