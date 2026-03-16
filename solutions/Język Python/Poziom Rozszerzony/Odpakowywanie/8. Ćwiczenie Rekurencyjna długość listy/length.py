
        
        
def length(sequence, i = 0):
    if bool(sequence) == True:
        i += 1
        _, *sequence = sequence
        return length(sequence, i)
    else:
        return i
