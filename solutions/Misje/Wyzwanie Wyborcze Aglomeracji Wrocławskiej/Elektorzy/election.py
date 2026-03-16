def sprawdzGlosy(dane, wyniki):
    suma_A = 0
    suma_B = 0
    for miejscowosc,radni, wynik_A, wynik_B in dane:
        if wynik_A > wynik_B:
            suma_A += radni
        else:
            suma_B += radni
            
    if suma_A == wyniki[0] and suma_B == wyniki[1]:
        return True
    else:
        return False
        
        
        