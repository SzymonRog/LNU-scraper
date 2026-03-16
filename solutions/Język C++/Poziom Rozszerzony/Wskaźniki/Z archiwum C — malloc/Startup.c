#include <stdint.h> // definicja typu size_t
unsigned long long* createEmptyUllArr(size_t size)
{
    return (unsigned long long*)calloc(size ,sizeof(unsigned long long));
}