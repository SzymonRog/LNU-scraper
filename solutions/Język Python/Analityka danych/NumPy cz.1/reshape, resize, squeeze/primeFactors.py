def primeFactors(number):
    result = []
    i = 2
    
    while i * i <= number:
        if number % i:
            i += 1
        else:
            result.append(i)
            number //= i
    
    if number > 1:
        result.append(number)
        
    return result