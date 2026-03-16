def read_good_letters(fname):
    napis = ""
    with open(fname) as file:
        for i in file.read():
            if i == "k":
               break
            else:
                napis += str(i)
                
                
    return napis