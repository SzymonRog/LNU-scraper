#include <cake.h>

void setAngle( int requiredWeight )
{
    float waga = getWeight();
    rotate(360*(requiredWeight/waga));
}
