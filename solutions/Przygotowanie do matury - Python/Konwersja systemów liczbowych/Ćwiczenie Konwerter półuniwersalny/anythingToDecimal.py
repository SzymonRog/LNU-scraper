def anythingToDecimal( x, k ):
    wynik = 0
    for znak in x:
        if '0' <= znak <= '9':
            cyfra = ord(znak) - ord('0')
        else:
            # A→10, B→11, ..., Z→35   (duże litery)
            cyfra = 10 + ord(znak.upper()) - ord('A')
        
        wynik = wynik * k + cyfra
    
    return wynik