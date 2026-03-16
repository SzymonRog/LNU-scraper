#include <string.h>

void strcpy_strcat()
{
    char str1[] = "Ala ma kota";
    char str2[30] = {'\0'};

    // kopiujemy str1 do str2
    strcpy( str2, str1 );
    std::cout << "Po skopiowaniu str1, str2 = " << str2 << std::endl;

    char str3[] = ", a kot ma Alę.";

    // dołączamy str3 do str2
    strcat( str2, str3 ); 
    std::cout << "Po dołączeniu str3, str2 = " << str2 << std::endl;

    // kopiujemy str2 do str1
    strncpy( str1, str2, strlen(str1) - 1 );
    std::cout << "Po skopiowaniu str2, str1  = " << str1 << std::endl;
}