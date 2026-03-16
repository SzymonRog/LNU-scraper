def checkIfCorrect(message, checkSum):
    suma = 0
    
    for i, znak in enumerate(message, start=1):  # numerujemy od 1
        kod = ord(znak)
        
        if i % 6 == 0:
            suma += kod * 6
        elif i % 3 == 0:
            suma += kod * 3
        elif i % 2 == 0:
            suma += kod * 2
        else:
            suma += kod
    
    obliczona_suma_kontrolna = suma % 256
    
    return obliczona_suma_kontrolna == checkSum