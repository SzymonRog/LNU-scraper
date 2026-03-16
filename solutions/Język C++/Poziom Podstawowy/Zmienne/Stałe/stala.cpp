#include <iostream>

using namespace std;

float obliczPredkosc( float czas )
{
    // tu zdefiniuj stałą g równą przyśpieszeniu ziemskiemu
    const float g = 9.81;
    return g * czas;
}

float wyswietl( float czas )
{
    float predkosc;
    predkosc = obliczPredkosc( czas );
    cout << "Po " << czas << "[ s ]" << endl;
    cout << "Prędkość = " << predkosc << "[ m/s ]";
    return predkosc;
}

