// Code here...
#include "Exhibit.hpp"
#include "Theme.hpp" 

int countDisplayed(const Exhibit exhibits[], int size, const Theme& theme) {
    // Sprawdzamy, czy tablica nie jest pusta
    if (exhibits == nullptr || size <= 0) {
        return 0;  // Zwracamy 0, jeśli tablica jest pusta
    }

    int count = 0;

    // Iterujemy przez tablicę eksponatów
    for (int i = 0; i < size; ++i) {
        // Jeśli eksponat jest na wystawie i pasuje do tematu
        if (exhibits[i].onDisplay && exhibits[i].theme == theme) {
            count++;  // Zwiększamy licznik
        }
    }

    return count;  // Zwracamy liczbę eksponatów na wystawie
}