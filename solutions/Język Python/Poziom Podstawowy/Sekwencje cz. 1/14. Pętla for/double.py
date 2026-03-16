def hasDuplicates( text ):
    for x in range(0, len(text) - 1):
        if (text[x] == text[x + 1]):
           return True
    return False
