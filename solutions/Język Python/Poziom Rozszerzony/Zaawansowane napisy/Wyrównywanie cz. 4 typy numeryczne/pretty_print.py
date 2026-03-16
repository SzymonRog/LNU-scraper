def pretty_print(indexes):
    for i in indexes:
        d_licz = len(str(i))
        dlugosc = 10 - d_licz
        print(f"{i:0=10}")