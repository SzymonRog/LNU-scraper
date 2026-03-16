#include "stacja_pogody.h"


float calc_mean()
{
    float temp = 0;
    float  ilosc_pom = 24 * 31 ;


    for (int x = 0; x <= 23; x++)
    {
        for(int y = 1; y<=31; y++)
        {
            temp += get_temp(x,y,3,2012);
        }
    }
                
    return  (temp/ilosc_pom);
}