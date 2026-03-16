def maxOrd( text ):
    y = 0
    for x in text:
        if ord(x) > y:
            y = ord(x)
    return y