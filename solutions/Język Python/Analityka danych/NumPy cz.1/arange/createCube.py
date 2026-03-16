import numpy as np

def createCube(length, value):
    # Krok 1: stwórz sześcian z liczbami od 1 do length**3
    cube = np.arange(1, length**3 + 1).reshape((length, length, length))
    
    # Krok 2: wypełnij wnętrze wartością 'value' (bez krawędzi)
    if length > 2:  # jeśli sześcian jest większy niż 2x2x2, bo inaczej wnętrze nie istnieje
        cube[1:-1, 1:-1, 1:-1] = value
    
    return cube
