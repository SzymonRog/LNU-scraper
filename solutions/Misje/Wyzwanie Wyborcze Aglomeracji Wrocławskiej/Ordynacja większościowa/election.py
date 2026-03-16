def sprawdzWyniki(a, b, c):
    numer = 0
    pierwszy  = []
    pie = 0
    dru = 0
    trze = 0
    
    for i in a:
        pie += i
    for i in b:
        dru += i
    for i in c:
        trze += i

    
        
    sum_głosów = pie + dru + trze
    kandydaci = [pie,dru,trze]
    
    for i in kandydaci:
        if 0.7 > round(int(i) / sum_głosów, 2) > 0.50:
            pierwszy.append(i)
        elif round(i / sum_głosów, 2 ) >= 0.7:
            numer = 4
        elif round(int(i) / sum_głosów, 2) <= 0.50:
            numer = 0
            
    if pie in pierwszy:
        numer = 1
    elif dru in pierwszy:
        numer = 2
    elif trze in pierwszy:
        numer = 3
            
            
    return numer
    
            