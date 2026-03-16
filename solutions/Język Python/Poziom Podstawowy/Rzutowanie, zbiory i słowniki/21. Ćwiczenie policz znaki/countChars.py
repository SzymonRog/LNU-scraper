def countChars( s ):
    d = dict.fromkeys(s.upper())
    for i in d:
        d[i] = s.upper().count(i)
    return d
        
    
