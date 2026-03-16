import random

def monte_carlo(population_size):
    points = []
    inside_circle = 0

    for _ in range(population_size):
        # Losowanie współrzędnych x i y w przedziale od 0 do 1
        x = random.random()
        y = random.random()
        points.append((x, y))

        # Sprawdzanie, czy punkt znajduje się wewnątrz okręgu
        distance = ((x - 0.5) ** 2 + (y - 0.5) ** 2) ** 0.5
        if distance <= 0.5:
            inside_circle += 1

    # Obliczenie przybliżonej wartości liczby pi
    pi_approx = 4 * (inside_circle / population_size)
    
    return points, pi_approx