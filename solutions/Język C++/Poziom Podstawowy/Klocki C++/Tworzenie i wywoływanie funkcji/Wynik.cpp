#include <iostream>

using namespace std;

void wyswietlWynik (int wynik)
{
    cout << wynik << endl;
}

int dodaj ( int a, int b )
{
    return ( a + b );
}

int dzienMiesiaca()
{
    short int a, b, wynik;
    a = 0;
    b = 2;
    wynik = dodaj ( a, b ); 
    wyswietlWynik ( wynik );
    return wynik;
}
