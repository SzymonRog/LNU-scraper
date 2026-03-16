
import lucas

def even_lucas_sum(n):
    suma = 0
    lista_znaków = lucas.lucas_up_to_n(n)
    for i in lista_znaków:
        if i % 2 == 0:
            suma += i
    return suma