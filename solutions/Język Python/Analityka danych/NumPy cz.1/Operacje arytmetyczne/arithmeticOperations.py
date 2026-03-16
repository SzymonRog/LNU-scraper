import numpy as np

def applyOperations(arr, operationsList):
    result = np.array(arr, dtype=float)
    base_shape = result.shape
    
    for other, op in operationsList:
        other_array = np.array(other, dtype=float)
        
        # TYLKO identyczny kształt
        if other_array.shape != base_shape:
            continue
        
        if op == "+":
            result = result + other_array
        elif op == "-":
            result = result - other_array
        elif op == "*":
            result = result * other_array
        elif op == "/":
            result = result / other_array
        elif op == "%":
            result = result % other_array
        elif op == "**":
            result = result ** other_array
        elif op == "//":
            result = result // other_array
    
    return result
