def largestInFile():
    
    with open("liczby.txt", "r") as file:
        liczby = []
        for line in file:
            content = line.split()
            liczby.append(int(content[0], int(content[1])))
            
    print(max(liczby))