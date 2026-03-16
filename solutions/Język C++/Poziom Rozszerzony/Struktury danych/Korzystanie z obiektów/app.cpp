#include <Book.hpp>
#include <Customer.hpp>
// Bierzemy referencje na obiekty, bo pozwoli to nam je modyfikować
bool buyBook(Customer& customer, Book& book)
{
    if(book.stockAmount > 0){
        if(customer.balance >= book.price){
            customer.balance -= book.price;
            book.stockAmount -= 1;
            return true;
        }
    }
    return false;
}