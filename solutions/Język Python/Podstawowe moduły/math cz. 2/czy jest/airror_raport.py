import math

def airror_raport(n):
    day_off = []
    for i in n:
        if math.isnan(n[i]):
            day_off.append(i)
            
    return day_off