def addSpace( value ):
    tekst = ""
    dlug = len(value)
    a = 1
    for i in value:
        if a == dlug:
            tekst += i 
            a+=1
        else:
            tekst += i + " "
            a+=1
    
    return tekst