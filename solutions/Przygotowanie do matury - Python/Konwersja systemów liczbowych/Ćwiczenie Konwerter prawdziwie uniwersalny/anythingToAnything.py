def anythingToAnything(x, k_in, k_out):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    # Konwertuj z k_in na dziesiętny
    decimal = 0
    for char in x.upper():
        decimal = decimal * k_in + digits.index(char)
    
    # Konwertuj z dziesiętnego na k_out
    if decimal == 0:
        return "0"
    
    result = ""
    while decimal > 0:
        result = digits[decimal % k_out] + result
        decimal //= k_out
    
    return result