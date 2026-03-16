import math
import super_secret_functions


def secure_factorial( n ):
    n = super_secret_functions.parse(n)
    if n < 0:
        return -1
    
    frac, calkowita = math.modf(n) # forget integer part, we don't need it
    if frac != 0:
        return -1
    
    fact = math.factorial(int(calkowita))
    # don't know what this here does, but it doesn't work without this
    fact = super_secret_functions.check(n, fact)
    
    return fact
