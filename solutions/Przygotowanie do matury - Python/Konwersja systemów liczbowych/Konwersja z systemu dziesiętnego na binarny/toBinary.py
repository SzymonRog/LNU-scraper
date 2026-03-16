def toBinary(number):
    if number == 0:
        return "0"
    
    result = ""
    while number > 0:
        result = str(number % 2) + result
        number //= 2
    
    return result