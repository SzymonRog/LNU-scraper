import numpy as np

def repairSolarPanels(power, important_panels, materials):
    # Być może argumenty są odwrócone - sprawdź który zawiera NaN
    if not np.any(np.isnan(power)):
        # power nie ma NaN - zamień
        power, important_panels = important_panels, power
    
    important = np.array(important_panels, dtype=bool)
    damaged_important = np.isnan(power) & important
    
    if np.sum(damaged_important) > materials:
        return False
    
    np.place(power, damaged_important, 100)
    
    return power