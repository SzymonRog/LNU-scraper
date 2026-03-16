// Tu zawarte są przykładowe testy do twojej funkcji.
// Mają za zadanie zademonstrować co jest oczekiwane od twojego rozwiązania.

#include <app.cpp>

// Sufiks _MSG dodany do EXPECT_EQ skutkuje wypisaniem 
// dodatkowych informacji w przypadku błędu

TEST(ExampleTests, CustomerCanBuyBook)
{
    Customer customer;
    customer.balance = 100;

    Book book;
    book.price = 50;
    book.stockAmount = 1;

    EXPECT_TRUE(buyBook(customer, book));
    EXPECT_EQ_MSG(customer.balance, 50);
    EXPECT_EQ_MSG(book.stockAmount, 0);
}

TEST(ExampleTests, CustomerOutOfMoney)
{
    Customer customer;
    customer.balance = 10;

    Book book;
    book.price = 50;
    book.stockAmount = 1;

    EXPECT_FALSE(buyBook(customer, book));

    EXPECT_EQ_MSG(customer.balance, 10);
    EXPECT_EQ_MSG(book.stockAmount, 1);
}

TEST(ExampleTests, BookOutOfStock)
{
    Customer customer;
    customer.balance = 100;

    Book book;
    book.price = 50;
    book.stockAmount = 0;

    EXPECT_FALSE(buyBook(customer, book));
    EXPECT_EQ_MSG(customer.balance, 100);
    EXPECT_EQ_MSG(book.stockAmount, 0);
}
