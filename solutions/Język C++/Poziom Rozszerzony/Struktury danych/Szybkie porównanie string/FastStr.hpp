#pragma once
#include <string>
#include <cstdint>

class FastStr {
public:
    static const int BASE = 26;        // Baza systemu (26 liter w alfabecie)
    static const uint64_t MOD = 1000000007; // Używamy dużego modułu, liczba pierwsza

    std::string text;
    uint64_t hashValue;

    // Konstruktor klasy, który automatycznie oblicza hash dla danego tekstu
    FastStr(const std::string& s = "") : text(s), hashValue(hash(s)) {}

    // Metoda do obliczenia wartości hasza dla tekstu
    uint64_t hash(const std::string& s) const {
        uint64_t result = 0;
        uint64_t power = 1;

        // Iteracja po wszystkich znakach tekstu
        for (char c : s) {
            result = (result + (alfaOrd(c) * power)) % MOD;
            power = (power * BASE) % MOD; // Zastosowanie modulo, aby uniknąć przepełnienia
        }
        return result;
    }

    // Metoda do obliczenia numeru porządkowego dla każdej litery
    int alfaOrd(char c) const {
        return c - 'a' + 1; // mapa: 'a' -> 1, ..., 'z' -> 26
    }

    // Operator porównania ==, porównujący teksty po haszach i samych tekstach
    bool operator==(const FastStr& other) const {
        return hashValue == other.hashValue && text == other.text;
    }
};

// Funkcja zmieniająca tekst w obiekcie FastStr
void changeStr(FastStr& fastStr, const std::string& newText) {
    fastStr.text = newText;
    fastStr.hashValue = fastStr.hash(newText);
}
