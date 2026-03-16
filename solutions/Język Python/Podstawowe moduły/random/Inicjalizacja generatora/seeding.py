import random
x = 1
random.seed(x)
print(random.randrange(0,1000))
random.seed(str(x))
print(random.randrange(0,1000))
random.seed(None)
print(random.randrange(0,1000))