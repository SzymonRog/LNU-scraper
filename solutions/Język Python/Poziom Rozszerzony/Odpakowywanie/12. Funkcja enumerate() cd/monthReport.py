def monthReport( data ):
    lis = []
    for i, (total, poz) in enumerate(data):
        if int(poz) / int(total) > 0.5:
            lis.append(int(i +1))
            
    return lis
            