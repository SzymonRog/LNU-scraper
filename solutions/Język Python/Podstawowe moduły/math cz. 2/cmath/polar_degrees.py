import cmath
import math

def polar_degrees(x, y):
    z = complex(x,y)
    
    phi_radians = cmath.phase(z)
    phi_degrees = math.degrees(phi_radians)
    
    if phi_degrees < 0:
        phi_degrees += 360
    
    
    if 0 < phi_degrees <= 90:
        return 1  
    elif 90 < phi_degrees <= 180:
        return 2  
    elif 180 < phi_degrees <= 270:
        return 3  
    elif 270 < phi_degrees <= 360 or phi_degrees == 0:
        return 4  
        
   