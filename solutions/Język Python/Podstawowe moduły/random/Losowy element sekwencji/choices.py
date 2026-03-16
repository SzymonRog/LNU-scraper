import random


def choices(population,k):
    lista = []
    i = 0
    while i < k:
        lista.append(random.choice(population))
        i += 1
    return lista