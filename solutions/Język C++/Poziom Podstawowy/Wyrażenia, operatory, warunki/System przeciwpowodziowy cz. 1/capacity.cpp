// Zadanie:
// Napisz program sterujący systemem zbiorników retencyjnych dla Centrum Zarządzania Kryzysowego, tak aby zminimalizować ryzyko powodzi w zlewni jednej z rzek. 
// Napisz funkcję calcAvailableCapacity, która jako wartość będzie zwracała objętość wody jaką zbiornik może przyjąć.
#include<reservoir_api.h>
int calcAvailableCapacity( E_RESERVOIRS reservoirs )
{
    int wysokosc = getLevel( reservoirs );
    int szerokosc = getWidth( reservoirs );
    int dlugosc = getLength( reservoirs );
    int capacity  = getCapacity( reservoirs );
    
    int ile_Zbiornik = wysokosc * szerokosc * dlugosc;
    return capacity - ile_Zbiornik ;
    
}
