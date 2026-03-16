def alphabetIndex( letter ):
    if "a" <= letter <= "z":
        return ord(letter) - 97
    else:
        return ord(letter) - 65