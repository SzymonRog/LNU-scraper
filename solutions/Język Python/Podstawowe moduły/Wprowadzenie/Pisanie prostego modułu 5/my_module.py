my_pi=3.14
import math
def incremented(n):
    """
    incremented() -- wypisuje komunikat o wartości liczby po inkrementacji
    """
    print(f"{n} plus jeden równa się {n+1}")
    
def solve_linear(a, b):
    if a==0:
        if b==0:
            print("nieskończenie wiele rozwiązań")
        else:
            print("sprzeczne")
    else:
        x=-b/a
        print(f"x jest równe {x}")
        
def my_sin(n):
    print(math.sin(math.radians(n)))