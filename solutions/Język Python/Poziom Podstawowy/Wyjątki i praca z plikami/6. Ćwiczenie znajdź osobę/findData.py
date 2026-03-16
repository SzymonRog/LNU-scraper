def findData( x ):
    file = open("data.txt", "r")
    y = file.readlines()
    file.close()
    for i in y:
        if i[0:11] == str(x):
            return i[12:-1]