import numpy as np

def calculateMemory(arr):
    return arr.size if arr.dtype == bool else arr.size * arr.itemsize * 8
