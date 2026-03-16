// Zadanie:
// Uruchom program.
// Przyjrzyj się komunikatom błędów i ostrzeżeń jakie wyświetlił kompilator w konsoli.
// Wróć do kodu i popraw wiersze, w których wystąpiły problemy, tak aby program prawidłowo się uruchomił.

#include <iostream>
using namespace std;

#define STALA 8

enum E_KULA
{
    BIALA = 0,
    CZERWONA = 1,
    CZARNA = 3,
    ZIELONA = 4,
    NIEBIESKA = 5,
    ROZOWA = 6,
};

bool bilard( int bila, E_KULA kula)
{
    bool wynik;
    switch (kula)
    {
    case ROZOWA: wynik = !( bila % 3 );
        break;
    case ZIELONA: wynik = ( bila == 5 );
    case BIALA: wynik = ( bila < 2 );
        break ;
    case CZERWONA: wynik = true;
        break;
    case CZARNA:wynik = ( bila == 7 );
    case NIEBIESKA: wynik = !bila;
        break;
    default: wynik = false;
    }
    cout << "Wynik = " << (wynik ? "true" : "false") << endl;
    return wynik;
}
