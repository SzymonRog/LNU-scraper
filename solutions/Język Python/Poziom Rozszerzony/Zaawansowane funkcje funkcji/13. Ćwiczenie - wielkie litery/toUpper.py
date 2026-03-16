#your code goes here
def toUpper(tekst, *litery):
    tekst_zamieniony = ""
    for i in tekst:
        if i.lower() in litery or i.upper() in litery:
            tekst_zamieniony += i.upper()
        else:
             tekst_zamieniony += i
             
    return tekst_zamieniony