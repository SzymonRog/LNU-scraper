def sumUp():
    f = open("data.txt", "r")
    x = f.readlines()
    s = 0 
    for i in x:
       s += float(i)
    f.close()
    return s
        
        
