import delivery
def keyPoints():
    y = set( delivery.get( delivery.robots()[0])['route'] )
    x = delivery.robots()
    for i in x:
        y &= set(delivery.get(i)['route'])
    if y == set():
        return 0 
    else:
        return y
        