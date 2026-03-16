// Zapewne napiszesz bardzo fajną funkcję
// Szkoda by było gdyby otrzymała wskaźnik na nullptr...

int getPtrInx(int* arr, int* ptr, int n) {
    // Sprawdzamy, czy wskaźnik ptr wskazuje na element tablicy
    if (ptr >= arr && ptr < arr + n) {
        // Jeśli tak, zwracamy indeks, który to jest w tablicy
        return ptr - arr;
    } else {
        // Jeśli ptr wskazuje poza tablicą, zwracamy -1
        return -1;
    }
}