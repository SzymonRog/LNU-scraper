#pragma once

#include <string>

/// @brief Przetworzy i wyświetli tekst na zewnętrznym wyświetlaczu
/// @param initials Wskaźnik do tekstu; Nic nie zostanie wyświetlone dla NULL
void displayBest(std::string* initials);

// TODO: Zrobić w końcu to drugie TODO
// TODO: Wymyśleć lepszą nazwę dla tej funkcji (nazwa nie jest precyzyjna)
/// @brief Przetworzy i wyświetli liczbę na zewnętrznym wyświetlaczu
/// @param n Najwyższy wynik testu
void displayBest(unsigned int n);