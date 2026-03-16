import delivery
def totalRoute():
    l = 0
    x = delivery.robots()
    for i in x:
        y = delivery.get(i)['data']['distanceToday']
        l += y
    return l
        