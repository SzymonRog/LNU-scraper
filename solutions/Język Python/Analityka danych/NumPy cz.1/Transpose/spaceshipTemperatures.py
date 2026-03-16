import numpy as np

def processData(spaceship_data):
    # wybieramy tylko temperaturę wewnętrzną (indeks 0)
    internal_temp = spaceship_data[:, :, 0]
    
    # zamieniamy osie: godziny ↔ moduły
    result = internal_temp.transpose()
    
    return result