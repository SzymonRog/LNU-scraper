def bmi( person ):
    _,_, m, w = person
    return round( m / ((w/100) ** 2), 2)