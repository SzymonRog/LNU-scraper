def toHexadecimal(number):
    digits = "0123456789ABCDEF"
    
    if number == 0:
        return "0x0"
    
    result = ""
    while number > 0:
        result = digits[number % 16] + result
        number //= 16
    
    return "0x" + result