#include <iostream>

using namespace std;

void wyswietl()
{
    enum ROSLINY {ROZA = 1, TULIPAN, KAKTUS};
    
    {
    };

    ROSLINY kwiat;
    kwiat = ROZA;
    cout << "Numer kwiatu = " << kwiat << endl;
    kwiat = TULIPAN;
    cout << "Numer kwiatu = " << kwiat << endl;
}
