import cmath

def quad_eq(a,b,c):
    if a == 0:
        return 0
    
    
    delta = cmath.sqrt(b**2 - 4*a*c)
    
    
    x1 = (-b + delta) / (2 * a)
    x2 = (-b - delta) / (2 * a)
    
    
    x1 = x1.real if x1.imag == 0 else x1
    x2 = x2.real if x2.imag == 0 else x2
    
    
    return x1,x2