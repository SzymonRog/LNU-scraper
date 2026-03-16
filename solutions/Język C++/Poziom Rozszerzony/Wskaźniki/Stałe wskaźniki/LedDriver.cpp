/* Zauważ, że jedna litera to jeden 'segment' w sygnale.
 *
 * Było by bardzo wygodnie gdybyś miał jakąś funkcję, np. hexToDec,
 * która zamieniłaby literę hexadecymalną na cyfrę.
 * 
 * Wtedy wystarczyło by odpowiednio poprzesuwać wyniki wywołań hexToDec...
*/

#include <iostream>

// Funkcja pomocnicza do konwersji z heksadecymalnej litery na cyfrę dziesiętną
unsigned int hexToDec(char hex) {
    if (hex >= '0' && hex <= '9') {
        return hex - '0'; // Dla cyfr 0-9
    } else if (hex >= 'A' && hex <= 'F') {
        return hex - 'A' + 10; // Dla liter A-F
    }
    return 0; // W przypadku błędnego znaku (można również rzucić wyjątek lub obsłużyć błąd)
}
unsigned int genSignalFromColor(const char* colors)
{
    if ( colors == nullptr)
    {
        return 0;
    }
    
     unsigned int red = (hexToDec(colors[0]) << 4) | hexToDec(colors[1]);
    
    // Kolejne 2 znaki to zielony (G)
    unsigned int green = (hexToDec(colors[2]) << 4) | hexToDec(colors[3]);
    
    // Ostatnie 2 znaki to niebieski (B)
    unsigned int blue = (hexToDec(colors[4]) << 4) | hexToDec(colors[5]);

    // Składamy 32-bitowy wynik:
    unsigned int result = (red << 16) | (green << 8) | blue;

    return result;


}
