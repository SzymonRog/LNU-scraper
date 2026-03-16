def who_failed(reports, thresholds):
    lis = []
    for  i, (imie, wynik) in enumerate(reports):
        if wynik >= thresholds[i]:
            pass
        else:
            lis.append(imie)
            
    return lis
            
        