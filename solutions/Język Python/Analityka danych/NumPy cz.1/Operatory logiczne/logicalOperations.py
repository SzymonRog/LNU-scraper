import numpy as np

def totalPower(produced_electricity, is_working):
    # Zamień na tablice NumPy, jeśli nie są jeszcze
    produced_electricity = np.array(produced_electricity)
    is_working = np.array(is_working, dtype=bool)
    
    # Utwórz maskę paneli, które działają i produkują >20
    mask = np.logical_and(is_working, produced_electricity > 20)
    
    # Zwróć sumę energii tych paneli
    return np.sum(produced_electricity[mask])
