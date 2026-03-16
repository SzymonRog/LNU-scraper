#pragma once

#include <string>

/// @param id Id produktu
/// @return Nazwa produktu
std::string getProductName(const int id);

/// @brief Przekonwertuje tablicę stringów do pojedynczego stringa i sformatuje wynik
/// @param arr Tablica zmiennych string; zostanie usunięta po użyciu
/// @param n Długość tablicy arr
/// @return Wynik 'spłaszczenia' tablicy
std::string flattenStringArray(std::string* arr, const size_t n);
