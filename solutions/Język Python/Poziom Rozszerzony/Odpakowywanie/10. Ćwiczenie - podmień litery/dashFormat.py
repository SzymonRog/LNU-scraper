def dashFormat( password_1, password_2, letter ):

    for p, i  in enumerate(password_1):
        if letter.upper == i.upper:
            password_2[p] = i
                
                
    return password_2
                
               