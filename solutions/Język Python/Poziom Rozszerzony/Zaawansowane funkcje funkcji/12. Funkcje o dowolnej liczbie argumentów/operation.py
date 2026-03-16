# Your code goes here
def operation(op, *liczby):
    s = 1
    for i in liczby:
        if op == '*':
            s = s * i
        else:
            s += i 
            
    if op == '*':
        return s
    else:
        return s - 1 
        
            
    