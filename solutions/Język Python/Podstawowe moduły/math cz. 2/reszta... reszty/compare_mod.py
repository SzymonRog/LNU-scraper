import math

def compare_mod(x, y):
    math_rem = math.remainder(x,y)
    math_fmod = math.fmod(x,y)
    return math_rem == math_fmod