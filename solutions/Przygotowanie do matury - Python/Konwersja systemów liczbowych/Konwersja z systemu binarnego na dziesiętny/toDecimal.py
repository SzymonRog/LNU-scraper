# Sposób 1 – pętla od lewej do prawej
def toDecimal(binary):
    wynik = 0
    for cyfra in binary:
        wynik = wynik * 2 + int(cyfra)
    return wynik