def sumOfElements( numbers ):
    num = iter(numbers)
    s = 0
    for i in num:
        s += int(i)
        
    return s
    