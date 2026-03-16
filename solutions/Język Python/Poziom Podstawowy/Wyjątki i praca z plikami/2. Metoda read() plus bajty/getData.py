def getData(x):
    plik = open("data.txt", "r" )
    x = plik.read(x)
    plik.close()
    return x