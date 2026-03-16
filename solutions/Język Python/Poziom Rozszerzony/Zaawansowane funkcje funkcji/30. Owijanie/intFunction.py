#your code goes here
zamiennik = int
def int(i):
    try:
        return zamiennik(i)
    except ValueError:
        return -1