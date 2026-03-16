def highLow( t1, t2 ):
    lista = t1 + t2
    male = sorted(lista, reverse = True)
    rosn = sorted(lista)
    n = male[0:3]
    m = sorted(rosn[0:3],reverse = True)
    return n + m