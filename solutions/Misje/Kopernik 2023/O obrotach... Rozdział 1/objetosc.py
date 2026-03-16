#Python
import math
from math import pi

def test( r ):
    pow_kula = 4 * pi * r**2
    bok_kwad = math.sqrt(pow_kula / 6)
    
    
    return ((4/3) * pi * r**3) - bok_kwad ** 3