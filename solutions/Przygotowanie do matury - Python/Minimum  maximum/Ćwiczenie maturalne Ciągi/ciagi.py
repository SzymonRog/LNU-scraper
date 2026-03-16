def ciagi():
    with open("ciagi.txt", "r") as file_ciagi:
        with open("wynik.txt", "w") as file_wynik:
            
            for line in file_ciagi:
                line = line.strip()
                
                #
                if line:
                    value = 0
                    znak = line[0]
                    liczby = line[1:].split()
                    liczby = [i for i in liczby if i]
                    liczby = [int(i) for i in liczby]
                        
                    if znak == "w":
                        value = max(liczby)
                    else:
                        value = min(liczby)
                        
                        
                    file_wynik.write(f"{value}\n")