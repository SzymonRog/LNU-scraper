def clearText( s ):
    znak = ""
    for x in s:
        if x.isalnum():
            znak += x 
    return znak