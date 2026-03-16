/* Notka:
 * 0 + '0' == '0'  // true
 * 5 + '0' == '5'  // true
 * 3 + '3' == '6' // true
 * 
 * Możemy tak zrboić, bo znaki (char) są ustawione 'po kolei'
 * W tabeli ASCII '0' ma numer 48, '1' - 49 i '9' - 57
 */

char* uintToChar(unsigned int liczba) {
    // Sprawdzamy, czy liczba jest 0
    if (liczba == 0) {
        char* arr = new char[2];  // Potrzebujemy 2 miejsca: '0' + '\0'
        arr[0] = '0';
        arr[1] = '\0';
        return arr;
    }

    // Obliczamy liczbę cyfr w liczbie
    unsigned int length = 0;
    unsigned int temp = liczba;
    while (temp > 0) {
        temp /= 10;
        length++;
    }

    // Tworzymy tablicę o odpowiednim rozmiarze (+1 na '\0')
    char* arr = new char[length + 1];

    // Wypełniamy tablicę cyframi
    arr[length] = '\0';  // Na końcu tablicy wstawiamy znak '\0'
    for (int i = length - 1; i >= 0; i--) {
        arr[i] = (liczba % 10) + '0';  // Zamiana cyfry na znak
        liczba /= 10;
    }

    return arr;
}