def avgPistachios( nuts ):
    dni = 0
    liczba = 0
    for i in nuts:
        liczba += i
        dni += 1
    return float(liczba/dni)