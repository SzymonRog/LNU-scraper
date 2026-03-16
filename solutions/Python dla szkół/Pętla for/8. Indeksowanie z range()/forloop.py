def everyThird( value ):
    tekst = ""
    for i in range(len(value)):
        if i % 3 == 0:
            tekst += value[i]
    return tekst