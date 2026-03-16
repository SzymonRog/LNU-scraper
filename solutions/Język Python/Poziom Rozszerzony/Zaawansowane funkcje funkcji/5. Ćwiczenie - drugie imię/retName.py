#your code goes 
def retName(first_name, family, second_name = 0 ):
    if  second_name:
        return first_name + " " + second_name +" "+ family
    else:
        return first_name + " " + family
    