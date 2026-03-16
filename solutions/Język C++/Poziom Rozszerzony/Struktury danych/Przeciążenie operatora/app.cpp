// Tutaj kot

#include "Time.hpp"

// Operator < do porównania obiektów Time
bool operator<(const Time& t1, const Time& t2)
{
    if (t1.hour != t2.hour)
        return t1.hour < t2.hour;  // Porównujemy godziny
    return t1.minute < t2.minute;  // Jeśli godziny są równe, porównujemy minuty
}