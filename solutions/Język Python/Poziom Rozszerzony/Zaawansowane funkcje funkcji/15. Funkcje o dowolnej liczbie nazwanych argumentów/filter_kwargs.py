# Your code goes here  
def filter_kwargs(modulo, **kwargs):
    lista = []
    for i in kwargs:
        if kwargs[i] % modulo == 0 :
            lista.append(str(i))
            
    return lista
            
            
    
    