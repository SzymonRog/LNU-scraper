import numpy as np

def processData(data):
    dt = [('temp', '<i4'), ('brightness', '<f8'), ('name', '<U15')]
    
    rec = np.rec.array(data, dtype=dt)
    
    mask = (rec.name == 'nieznana') & (rec.temp > 5700)
    
    return rec[mask]