import math

def find_near(value, collection, tol):
    tolerance_num = []
    for number in collection:
            if math.isclose(value, number, rel_tol = tol):
                tolerance_num.append(number)
                
    return tolerance_num