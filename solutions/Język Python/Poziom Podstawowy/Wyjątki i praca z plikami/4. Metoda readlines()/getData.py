def getData( fileName ):
    file = open( fileName , "r" )
    x = file.readlines()
    val = ""
    for y in x:
        val += y[0]
    file.close()
    return val