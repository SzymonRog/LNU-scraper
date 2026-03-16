def quinaryToDecimal(quinary):
    wynik = 0
    for cyfra in quinary:
        wynik = wynik * 5 + int(cyfra)
    return wynik