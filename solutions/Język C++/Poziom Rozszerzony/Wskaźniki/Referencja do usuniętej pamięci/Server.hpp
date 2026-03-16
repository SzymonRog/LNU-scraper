/// @brief Funkcja pobiera imię użytkownika o podanym id.
/// @return Wskaźnik na stałą tablicę znaków.
///         Jeśli użytkownik o podanym id nie istnieje zwrócony zostanie nullptr
const char* getUserName(const int id);

/// @brief Funkcja pobiera nazwisko użytkownika o podanym id.
/// @return Wskaźnik na stałą tablicę znaków.
///         Jeśli nazwisko nie istnieje, zwraca nullptr.
const char* getUserSurname(const int id);