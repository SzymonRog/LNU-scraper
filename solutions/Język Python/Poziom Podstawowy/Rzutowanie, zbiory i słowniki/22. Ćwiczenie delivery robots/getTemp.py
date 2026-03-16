import delivery
def getTemp( x ):
    y = delivery.get(x)
    z = y['data']['engineTemp']
    return z