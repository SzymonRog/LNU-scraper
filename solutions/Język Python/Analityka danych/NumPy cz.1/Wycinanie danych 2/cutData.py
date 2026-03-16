import numpy as np

def dataSlice(data, tempRange, pressureRange, testsRange):
    # zakres temperatur
    if tempRange is None:
        t_start, t_stop = None, None
    else:
        t_start = tempRange[0] + 250
        t_stop  = tempRange[1] + 250

    # zakres ciśnienia
    if pressureRange is None:
        p_start, p_stop = None, None
    else:
        p_start = pressureRange[0] - 50
        p_stop  = pressureRange[1] - 50

    # zakres testów
    if testsRange is None:
        s_start, s_stop = None, None
    else:
        s_start, s_stop = testsRange

    return data[t_start:t_stop, p_start:p_stop, s_start:s_stop]
