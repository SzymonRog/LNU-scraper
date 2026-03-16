import math

def check_value(value, lower_lim, upper_lim):
    if value >= lower_lim and value <= upper_lim:
        return value
    elif value < lower_lim:
        return -math.inf
    else:
        return math.inf