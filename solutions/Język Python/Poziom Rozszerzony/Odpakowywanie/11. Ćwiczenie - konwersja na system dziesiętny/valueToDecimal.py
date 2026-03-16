def valueToDecimal(value, base):
    result = 0 
    for i , el in enumerate(value[::-1]):
        result += int(el) * base ** i 
        
    return result
        