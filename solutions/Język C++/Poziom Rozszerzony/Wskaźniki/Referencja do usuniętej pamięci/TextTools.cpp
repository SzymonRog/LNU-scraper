#include <Server.hpp>
#include <string>
#include <cctype>

using namespace std;

// Funkcja wywoływana jest w innych miejscach interfejsu.
// Nie zmieniaj jej działania dla poprawnych danych.
string formatInitials(const char& name, const char& surname)
{
    string res = "";
    res.push_back(toupper(name));
    res.push_back('.');

    if (surname != '\0') {
        res.push_back(toupper(surname));
        res.push_back('.');
    }

    return res;
}

string getReceiversInitials(const int* ids, size_t len)
{
    string result = "";

    for (size_t i = 0; i < len; i++)
    {
        const char* name = getUserName(ids[i]);
        const char* surname = getUserSurname(ids[i]);

        // User does not exist - no initials
        if (!name || !*name)  // Sprawdzamy, czy imię jest puste
        {
            continue;  // Przechodzimy do następnego użytkownika, jeśli imię jest puste
        }

        if (surname && *surname) {
            // Oba dane istnieją (imię i nazwisko)
            result += formatInitials(name[0], surname[0]);
        } else {
            // Tylko imię, brak nazwiska
            result += formatInitials(name[0], '\0');  // Przekazujemy '\0' zamiast nazwiska
        }

        if (i != len - 1)
        {
            result += " ";  // Dodajemy spację między inicjałami
        }
    }

    return result;
}
