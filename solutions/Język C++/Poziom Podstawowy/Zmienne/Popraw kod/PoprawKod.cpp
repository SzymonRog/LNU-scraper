//
// Zabawa : Popraw kod źródłowy
//

float msTokmh( float MS )
{
    float km_h = ( MS * 3600 ) / 1000;
    return km_h;
}

float obliczPredkosc( float czas, float droga )
{
    float predkosc = 1.0;
    predkosc = droga / czas;
    return predkosc;
}

float poprawKod( float czas, float droga )
{
    float predkosc = obliczPredkosc( czas, droga );
    predkosc = msTokmh( predkosc );
    return predkosc;
}
