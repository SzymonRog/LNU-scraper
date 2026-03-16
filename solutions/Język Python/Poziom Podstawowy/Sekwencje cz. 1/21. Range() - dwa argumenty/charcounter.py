def charsInDoc(a, b):
    y = 0
    for x in range( a, b +1):
        y += charsOnPage(x)
    return y