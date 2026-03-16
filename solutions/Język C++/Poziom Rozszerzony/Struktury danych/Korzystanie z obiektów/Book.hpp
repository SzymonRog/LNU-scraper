#include <string>

struct Book
{
    std::string title;
    std::string author;

    std::string ISBN;
    unsigned int numOfPages;

    float price;
    unsigned int stockAmount;

    bool isPaperback;
};
