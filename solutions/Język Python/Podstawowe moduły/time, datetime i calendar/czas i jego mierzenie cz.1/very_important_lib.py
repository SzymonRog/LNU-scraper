import time

def very_important_func():
    def fib(n):
        if n <= 1:
            return n
        else:
            return fib(n - 1) + fib(n - 2)
    
    [fib(n) for n in range(1, 31)]