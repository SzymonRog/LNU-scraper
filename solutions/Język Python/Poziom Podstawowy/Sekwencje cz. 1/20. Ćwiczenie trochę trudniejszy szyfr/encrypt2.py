def encrypt( message ):
    y=""
    for x in range(len(message)):
        y += chr( ord( message[ x ] ) + x )
    return y