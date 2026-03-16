def pretty_print(report):
    dlugosc = max([len(imie) for imie in report.keys()])
    for imie, wynik in report.items():
        if dlugosc < len(imie):
            dlugosc = len(imie) 
        print (f"{imie:{dlugosc}} {wynik}")
        