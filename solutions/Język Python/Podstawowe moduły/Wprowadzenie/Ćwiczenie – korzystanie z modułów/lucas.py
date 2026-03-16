LUCAS_1 = 2
LUCAS_2 = 1


def nth_lucas(n):
    a = LUCAS_1
    b = LUCAS_2
    for i in range(n-1):
        a, b = b, a+b
    return a


def lucas_up_to_n(n):
    result = []
    a = LUCAS_1
    b = LUCAS_2
    for i in range(n-1):
        result.append(a)
        a, b = b, a+b
    result.append(a)
    return result
