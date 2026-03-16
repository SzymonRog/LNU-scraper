import numpy as np

def reinterpret_bytes(arr: np.ndarray) -> np.ndarray:
    if arr.dtype != np.uint8:
        raise TypeError("Wejście musi być tablicą typu np.uint8")
    if arr.size != 8:
        raise ValueError("Tablica musi zawierać dokładnie 8 bajtów")

    # reinterpretacja tych samych bajtów jako float64
    return arr.view(np.float64)
