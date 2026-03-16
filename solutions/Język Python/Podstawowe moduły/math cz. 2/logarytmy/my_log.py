import math

def my_log(number, base):
    if base == 2:
        return math.log2(number)
    elif base == 10:
        return math.log10(number)
    else:
        return math.log(number,base)