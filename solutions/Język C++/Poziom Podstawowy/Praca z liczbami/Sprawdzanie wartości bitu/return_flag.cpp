#include <cmath>
bool return_flag (unsigned char flags, int flag)
{
    unsigned char maska = pow(2,flag);
    if ((flags & maska) == maska)
        return true;
    else
        return false;
}
