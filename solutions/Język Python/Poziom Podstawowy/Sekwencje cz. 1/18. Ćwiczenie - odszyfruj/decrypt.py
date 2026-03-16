def decrypt( message, key):
    y = ""
    for x in message:
        y += chr( ord(x) // key)
    return y
    
    