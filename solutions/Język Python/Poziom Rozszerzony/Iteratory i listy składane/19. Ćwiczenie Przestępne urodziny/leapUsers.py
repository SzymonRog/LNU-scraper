def leapUsers( users ):
    return sum([ int(i[:4]) % 4 == 0 for i in users if int(i[:4]) % 100 != 0 or int(i[:4]) % 400])