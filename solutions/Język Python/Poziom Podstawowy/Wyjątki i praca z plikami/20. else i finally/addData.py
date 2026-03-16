def addData(x):
    file = open("data.txt", "a+")
    try:
        file.write( x )
    except:
        return "Type error"
    return "Done"
        
   
