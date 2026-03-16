def getData( x ):
    plik = open( "data.txt", "r" )
   
    
    for i in range(x):
        y = plik.readline()
    plik.close()
    return y
    