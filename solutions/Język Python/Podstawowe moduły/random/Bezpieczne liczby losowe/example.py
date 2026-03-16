from mersenne_cracker import recover_state
import random


# Przesuwamy stan początkowy dla utrudnienia odgadnięcia stanu
for i in range(371):
    random.random()

# Generujemy trochę danych, które wykorzytsane zostaną do odgadnięcia
vec = [random.getrandbits(32) for i in range(624)]

newrand = random.Random()
newrand.setstate(recover_state(vec))


# Wypisujemy prawdziwe i przewidiane wartości
real_value = random.random()
predicted_value = newrand.random()
print(f"Prawdziwa wartość:\n\t{real_value}")
print(f"Przewidziana przez nas wartość:\n\t{predicted_value}\n")

real_value = random.sample(range(1024), 16)
predicted_value = newrand.sample(range(1024), 16)
print(f"Prawdziwa wartość:\n\t{real_value}")
print(f"Przewidziana przez nas wartość:\n\t{predicted_value}\n")