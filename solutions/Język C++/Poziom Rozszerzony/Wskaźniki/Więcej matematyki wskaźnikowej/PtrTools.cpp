/* Funkcji do napisania jest 'więcej niz zwykkle'.
 * Na szczęście nie musisz napisać wszystkich od razu, 
 * a nawet sama zawartość funkcji może być pisana krok po kroku.
 *
 * Spróbuj pobawić się w "TDD" - Pisanie kodu w małych krokach tak, by za każdym
 * razem przechodził więcej testów.
 * Do TDD jeszcze 'kiedyś' wrócimy
 */

int* next(int* ptr, unsigned int n = 1) {
    // Sprawdzenie, czy wskaźnik jest nie-null
    if (ptr == nullptr) return nullptr;
    return ptr + n;  // Przesuwamy wskaźnik o n elementów do przodu
}

int* prev(int* ptr, unsigned int n = 1) {
    // Sprawdzenie, czy wskaźnik jest nie-null
    if (ptr == nullptr) return nullptr;
    return ptr - n;  // Przesuwamy wskaźnik o n elementów do tyłu
}

int* middle(int* l, int* r) {
    // Sprawdzamy, czy wskaźniki są prawidłowe i w odpowiedniej kolejności
    if (l == nullptr || r == nullptr || l > r) return nullptr;
    // Zwracamy wskaźnik na element pomiędzy
    return l + (r - l) / 2;
}