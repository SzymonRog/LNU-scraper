import math 

def my_distance(p, q):
    dlug1 = len(q)
    dlug2 = len(p)
    p_sum = sum(p)
    q_sum = sum(q)
    if dlug1 != dlug2:
        return "Błąd: punkty w różnych wymiarach"
    elif p_sum == 0:
        return math.hypot(q)
    elif q_sum == 0:
        return math.hypot(p)
    else:
        return math.dist(p,q)
    