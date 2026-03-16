#include <stdio.h>

void funkcja_printf()
{
    char str1[] = "Ala ma kota\n";
    printf( "%s", str1 );       // Wyświetlamy tekst

    int value = 5;
    printf( "%d\n", value );    // Wyświetlamy wartość całkowitą

    float pi = 3.1416;
    printf( "%f\n", pi );       // Wyświetlamy  wartość typu float 

    // Wyświetlamy tekst i wartość typu float z formatowaniem - szerokość pięć, dwa miejsca po przecinku
    printf( "%s %5.2f\n", "Pi = ", pi );
}