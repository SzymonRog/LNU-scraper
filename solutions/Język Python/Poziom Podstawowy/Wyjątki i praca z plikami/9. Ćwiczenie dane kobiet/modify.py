def modify():
    file = open("women.txt", "r")
    p = file.readlines()
    file.close()
    file = open("women.txt", "w")
    for i in p:
        if int(i[9]) % 2 == 0:
            file.write(i)
    file.close()
    
        