import numpy as np

def compareArrays(arr1, arr2):
    arr1 = np.array(arr1)
    arr2 = np.array(arr2)
    
    # Sprawdzenie czy tablice są identyczne
    if np.array_equal(arr1, arr2):
        return 4
    
    # Liczba miejsc, gdzie arr1 > arr2 i arr2 > arr1
    arr1_greater = np.sum(arr1 > arr2)
    arr2_greater = np.sum(arr2 > arr1)
    
    # Tablice równe pod względem liczby większych elementów
    if arr1_greater == arr2_greater:
        return 3
    elif arr1_greater > arr2_greater:
        return 1
    else:
        return 2
