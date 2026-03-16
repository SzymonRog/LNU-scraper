#your code goes here
def grossPrice(n, p = 0 ):
    if p:
        return round(n + (n * (p / 100)) , 2)
    else:
        return round(n * 1.23, 2)
