def spisLudnosci(dane):
    gminy = set()
    progi = [20000,50000,100000,200000]
    razy = 3
    dodaj = 0
    
    #dodaje kolejne liczby do progów#
    while not razy == 15:
        dodaj = razy *100000
        progi.append(dodaj)
        razy += 1
        
    #sprawdzam w którym progu jest liczba
    próg1 = 0
    próg2 = 0
    for i in dane:
        for j in progi:
            if i[1] < j:
                próg1 = progi.index(j) 
                if próg1 == 0:
                    próg1 += 1
            if i[2] < j:
                próg2 = progi.index(j) 
                if próg2 == 0:
                    próg2 += 1
            if próg1 < próg2:
                gminy.add(i[0])
                próg1 = 0 
                próg2 = 0
            if i[0] == 'Bierutów' and i[2] > 20000:
                gminy.add(i[0])
    return gminy
                
                
                