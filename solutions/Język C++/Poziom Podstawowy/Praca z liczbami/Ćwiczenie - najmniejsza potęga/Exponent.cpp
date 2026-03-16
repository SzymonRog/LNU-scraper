#include <cmath>
unsigned int find_exponent( unsigned int base, unsigned int value)
{
    int wykladnik = 0;
    bool lowest  = true;
    while (lowest)
    {
        if( value < pow(base, wykladnik))
            lowest = false;
            
        wykladnik++;
    }
    return wykladnik - 2;
}
