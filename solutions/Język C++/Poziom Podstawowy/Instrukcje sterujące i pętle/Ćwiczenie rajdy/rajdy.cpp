#include<rajdy.h>

float average_speed( int check_points )
{
    double czas = 0;
    double dlugosc = 0;
    for(int i = 1;i <= check_points;i++)
    {
        czas += get_time(i);
        dlugosc += get_length(i);
    }
    
    double predkosc_ms =  dlugosc / czas;
    double predkosc_kmh = (predkosc_ms * 3600) / 1000;
    return predkosc_kmh;
}