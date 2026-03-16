#place for your code
def  delKeys(słownik,*do_usunięcia ):

    for i in do_usunięcia:
        if i in słownik:
            del słownik[i]
    return słownik
    
