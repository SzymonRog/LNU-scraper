def whatSystem(x, num):
    # Funkcja pomocnicza do zamiany litery na cyfrę
    def char_to_digit(c):
        if '0' <= c <= '9':
            return int(c)  # Cyfry 0-9
        return ord(c.upper()) - ord('A') + 10  # Litery A-Z jako cyfry 10-35
    
    # Zmienna max_digit to maksymalna cyfra w liczbie x (z uwzględnieniem liter A-Z)
    max_digit = max(char_to_digit(digit) for digit in x)
    
    # Sprawdzamy kolejne podstawy systemów liczb
    for base in range(max_digit + 1, 37):  # Szukamy podstawy od max_digit + 1 do 36 (bo możemy mieć cyfry 0-9 i A-Z)
        try:
            # Konwertujemy liczbę z systemu o podstawie 'base' na system dziesiętny
            value = int(x, base)
            # Jeśli uzyskana wartość jest równa num, to zwracamy tę podstawę
            if value == num:
                return base
        except ValueError:
            # Jeżeli konwersja nie powiedzie się, to przechodzimy do kolejnej podstawy
            continue
    
    # Jeśli nie znajdziemy pasującej podstawy
    return -1