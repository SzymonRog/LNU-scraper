def encrypt( message ):
    y = ""
    for x in message:
        ord(x)
        y += chr(ord(x) * 2)
    return y