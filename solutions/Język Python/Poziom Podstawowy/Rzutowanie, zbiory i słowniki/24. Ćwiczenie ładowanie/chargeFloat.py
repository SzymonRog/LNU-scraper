import delivery
def chargeFloat():
    x = delivery.robots()
    for i in x:
        if delivery.get(i)['data']['batteryCharge'] < 25:
            delivery.charge(i)
   