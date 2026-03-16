/* Na razie klasy zaznaczać będziemy keywordem 'struct'.
 * Jego działanie różni się nieco od 'class', ale o tym przy obiektach */

// Nazwy klas - jako ważnych elementów - zaznaczane będą PascalCase'em
#include<string>
using namespace std;

struct Book
{
    string title;
    string author;
    string ISBN;
    unsigned int numOfPages;
    float price;
    unsigned int stockAmount;
    bool  isPaperback;
    
    
    // Tu należy umieszczać pola klasy

};
// Pamiętaj o średniku
