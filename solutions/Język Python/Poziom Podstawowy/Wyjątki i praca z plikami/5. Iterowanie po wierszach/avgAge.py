def avgAge():
    file = open("data.txt", "r")
    x = file.readlines()
    z = 0 
    y = 0
    for i in x:
        z += float(i[0:2])
        y += 1
    avg = z / y
    file.close()
    return avg