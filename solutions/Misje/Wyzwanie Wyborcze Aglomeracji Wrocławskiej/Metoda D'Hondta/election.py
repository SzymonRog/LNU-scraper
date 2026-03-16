def testDhondta(glosy):
    suma_glosow = sum(glosy)
    mandaty = 77
    
    # Sprawdzam, które partie przekroczyły próg 5%
    partie = [i for i in range(len(glosy)) if glosy[i] / suma_glosow >= 0.05]
    
    # Jeśli nie ma żadnych partii, które przekroczyły próg, zwróć pustą listę mandatów
    if not partie:
        return [0] * len(glosy)
    
    # Listę ilorazów będziemy liczyć dla każdej partii z osobna
    dzielenie = []
    for i in partie:
        for dzielnik in range(1, mandaty + 1):
            dzielenie.append((glosy[i] / dzielnik, glosy[i], i))  # (iloraz, liczba głosów, indeks partii)
    
    # Sortuję ilorazy w taki sposób, by w przypadku remisu wybrać partię z większą liczbą głosów
    dzielenie.sort(reverse=True, key=lambda x: (x[0], x[1], -x[2]))  # Sortowanie: iloraz, liczba głosów, indeks
    
    # Przydzielanie mandatów
    przydzial = [0] * len(glosy)  # Tworzę listę do przechowywania liczby mandatów dla każdej partii
    
    # Przydzielam 77 mandatów na podstawie posortowanych ilorazów
    for _, _, index in dzielenie[:mandaty]:
        przydzial[index] += 1
    
    return przydzial
        
    
    
            
    
    
    
    