def convertList(values, bases):
    wrong = []
    for i in range(len(values)):
        try:
            int(str(values[i]), bases[i])
        except:
            wrong.append(values[i])
            
    return wrong