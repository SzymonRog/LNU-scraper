import math

def uni_trig(func, degrees, ftype=''):
    radians = math.radians(degrees)
    
    
    if ftype == '':
        if func == 'sin':
            return math.sin(radians)
        elif func == 'cos':
            return math.cos(radians)
        elif func == 'tan':
            if degrees % 180 == 90:  
                return "błąd - wynik nie istnieje"
            return math.tan(radians)
        elif func == 'cotan':
            if degrees % 180 == 0:  
                return "błąd - wynik nie istnieje"
            return 1 / math.tan(radians)

    
    elif ftype == 'h':
        if func == 'sin':
            return math.sinh(radians)
        elif func == 'cos':
            return math.cosh(radians)
        elif func == 'tan':
            return math.tanh(radians)
        elif func == 'cotan':
            sinh_value = math.sinh(radians)
            if sinh_value == 0:  
                return "błąd - wynik nie istnieje"
            return math.cosh(radians) / sinh_value

    
    return "błąd - nieznana funkcja"