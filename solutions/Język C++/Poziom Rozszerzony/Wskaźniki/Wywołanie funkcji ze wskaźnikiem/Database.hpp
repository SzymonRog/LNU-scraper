#pragma once

#include <string>

/// @brief Sprawdza czy login jest zajęty
///
/// @details Odwołuje się do bazy danych przez proxy w celu wykonania zapytania.
///          Jeśli parametr jest nullptr, funkcja zwróci false.
/// @param str Wskaźnik na login do sprawdzenia
/// @return true jeśli login jest zajęty, false w przeciwnym wypadku
bool isLoginUsed(const std::string* str);