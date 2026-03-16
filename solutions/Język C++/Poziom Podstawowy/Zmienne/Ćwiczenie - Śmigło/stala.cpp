#include <iostream>

using namespace std;

float propeller_speed( float length )
{
    const float pi = 3.1415;
    return 2 * pi * length;
}

void wyswietl()
{
    float dlugosc = 15;
    cout << "Prędkość śmigła = " << propeller_speed( dlugosc ) << " [ m/s ]";
}
