#Twój program:
def sprawdz_trojkat(x, y, z):
    if  x + y > z and y < x + z and x < z + y:
        return True
    else:
        return False

        
