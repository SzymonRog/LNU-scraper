def cleanup(string):
    letter_iterator = iter(string)
    x = ""
    while True:
        try:
            l = next(letter_iterator)
            if l.isalnum():
                x += l
        except  StopIteration:
            break
        
    return x