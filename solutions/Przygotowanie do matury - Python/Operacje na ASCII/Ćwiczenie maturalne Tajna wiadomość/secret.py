def secret():
    with open("slowa.txt", "r") as file:
        słowa = []
        for line in file:
            słowo = ""
            for znak in line:
                if not (ord(znak) % 5) == 0:
                    słowo += znak
                    
            słowa.append(słowo)
            
            
        with open("wynik.txt", "w") as wynik_file:
            for słowo in słowa:
                wynik_file.write(f"{słowo}\n")