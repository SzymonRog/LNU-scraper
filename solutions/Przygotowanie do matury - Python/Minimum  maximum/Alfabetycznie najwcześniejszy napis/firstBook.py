def firstBook( titles ):
    alph = "z"
    for i in titles:
        if i < alph:
            alph = i
    return alph