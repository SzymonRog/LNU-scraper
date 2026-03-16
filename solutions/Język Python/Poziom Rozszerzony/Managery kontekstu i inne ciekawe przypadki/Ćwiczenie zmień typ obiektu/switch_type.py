def switchType(arg):
    
    if type(arg) in (int, float):
        return str(arg)
    else:
        try:
            return int(arg)
        except:
            return float(arg)