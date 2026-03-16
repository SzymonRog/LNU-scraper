def invert(transform, output, n=100):
    guess = output
    for _ in range(n):
        newguess = transform(guess)
        if newguess == output:
            return guess
        guess = newguess
    raise ValueError(f"{output} not invertible in {n} tries")

# Transformacje wykonywane wewnętrznie przez MT19937
# Algorytm może być wykorzystany do odtworzenia stanu generatora
#  innych wersji algorytmu Mersenne Twister
# W tym celu wystarczy podmienić transformacje na odpowiednie dla danego algorytmu
t1 = lambda y: y ^ (y >> 11)
t2 = lambda y: y ^ ((y << 7) & 0x9d2c5680)
t3 = lambda y: y ^ ((y << 15) & 0xefc60000)
t4 = lambda y: y ^ (y >> 18)

def invert_mt(y):
    y = invert(t4, y)
    y = invert(t3, y)
    y = invert(t2, y)
    y = invert(t1, y)
    return y

def recover_state(vec):
    if len(vec) != 624:
        raise ValueError("Passed argument `vec` has to be a sequence of length 624")
    return (3,
            tuple(map(invert_mt, vec)) + (624,),
            None)
