def format():
    file = open("data.txt", "r")
    x = file.readlines()
    file.close()
    file = open("data.txt", "a")
    x.reverse()
    for i in x:
        file.write(i)
    file.close
        
    
