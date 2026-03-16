def dzien_tygodnia( x ):
    d = ""
    if x == 1:
        d = "poniedziałek"
    elif x == 2:
        d = 'wtorek'
    elif x == 3:
        d = "środa"
    elif x == 4:
        d = "czwartek"
    elif x == 5:
        d = 'piątek'
    elif x == 6:
        d = "sobota"
    elif x == 7:
        d= "niedziela"
        
    else:
        d = "błąd"
    
    return d