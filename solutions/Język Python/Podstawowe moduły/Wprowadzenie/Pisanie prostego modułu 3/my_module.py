def incremented(n):
    """
    incremented() -- wypisuje komunikat o wartości liczby po inkrementacji
    """
    print(f"{n} plus jeden równa się {n+1}")
    
    
def solve_linear(a, b):
    if a==0 and b!=0:
        print("sprzeczne")
    elif a ==0 and b == 0:
        print("nieskończenie wiele rozwiązań")
    else:
        print(f"x jest równe {-(b)/a}")