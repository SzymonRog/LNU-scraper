from dataDispenser import nextValue

def analyze(size):
    suma = 0
    wart = 0
    for i in range(size):
        if (wart:= nextValue()) > 3.14:
            suma += wart
    return suma
    