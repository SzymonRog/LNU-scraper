def intPlusFract( list_1, list_2 ):
    new_list = list( map(lambda x,y: float(str(x) + "." + str(y)), list_1, list_2))
    return new_list