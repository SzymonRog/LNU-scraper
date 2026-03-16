from functools import singledispatch

@singledispatch
def count_elements(container):
    ilość = len(container)
    return(ilość)
    
@count_elements.register
def _(arg: str):
    słowa = 1
    for i in arg:
        if i == " ":
            słowa += 1
    return słowa

@count_elements.register
def _(arg: dict):
    ile_elementów = 0
    for i in arg:
        ile_elementów += 2
        
    return ile_elementów
    

    