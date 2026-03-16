// Zadanie:
// Napisz funkcję, która zwraca wyrażoną w m3 objętość wody niesioną przez rzekę w ciągu sekundy w określonym punkcie kontrolnym.
#include<reservoir_api.h>
int calcRiverCapacity( E_RESERVOIRS reservoirs )
{
    int predkosc = getRiverSpeed( reservoirs );
    int szerokosc = getRiverLevel( reservoirs );
    int wysokosc = getRiverWidth( reservoirs );
    int capacity = predkosc * szerokosc * wysokosc;
    return capacity;
}



