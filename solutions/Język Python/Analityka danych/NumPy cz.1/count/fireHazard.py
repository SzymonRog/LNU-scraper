import numpy as np

def fireRisk(temperature, humidity):
    temperature = np.array(temperature)
    humidity = np.array(humidity)

    # III stopień: jeden warunek wystarczy
    risk3 = np.logical_or(humidity <= 30, temperature > 35)

    # II stopień: jeden warunek, ale wykluczamy już III
    risk2 = np.logical_or(np.logical_and(humidity >= 31, humidity <= 50),
                          np.logical_and(temperature >= 28, temperature <= 35))
    risk2 = np.logical_and(risk2, ~risk3)

    # I stopień: jeden warunek, wykluczamy II i III
    risk1 = np.logical_or(np.logical_and(humidity >= 51, humidity <= 80),
                          np.logical_and(temperature >= 21, temperature <= 27))
    risk1 = np.logical_and(risk1, ~(risk2 | risk3))

    # 0 stopień: wszystko pozostałe
    risk0 = ~(risk1 | risk2 | risk3)

    return [
        np.count_nonzero(risk0),
        np.count_nonzero(risk1),
        np.count_nonzero(risk2),
        np.count_nonzero(risk3)
    ]
