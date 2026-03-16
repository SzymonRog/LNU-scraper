def addData(x):
    p = open("data.txt", "a")
    p.write(str(x['PESEL']) + ' ' + x['firstName'] + ' ' + x['familyName'] + '\n')
    p.close()