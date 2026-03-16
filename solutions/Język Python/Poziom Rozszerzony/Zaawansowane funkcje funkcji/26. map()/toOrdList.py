def toOrdList(text):
    new_text =  set(map(lambda i: ord(i), text) )
    return new_text