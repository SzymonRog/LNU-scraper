def replaceSign(x, y):
    f1 = open("data.txt", "r+")
    z = f1.read()
    for i in  range(len(z)):
        if z[i] == x:
            f1.seek(i)
            f1.write(y)
            
    f1.close()
   