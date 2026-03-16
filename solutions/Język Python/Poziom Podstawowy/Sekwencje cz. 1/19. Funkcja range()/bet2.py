def prize( days ):
    money = 0 
    suma = 0
    for x in range(days):
        money += x + 1
        suma += money 
    return suma
        