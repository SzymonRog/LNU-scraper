// Ta linijka zaznacza, że plik ma zostać uwzględniony w programie tylko raz,
// jeszcze do tego wócimy...
#pragma once
#include <string>
#include <stdint.h>
#include <cstdint>
#include <Item.hpp>

class Order {
public:
    uint32_t tableId = 0;
    uint32_t numOfCustomers = 0;
    uint32_t numOfItems = 0;
    Item* orderedItems = nullptr;
    float paymentDue = 0.0f;
    std::string annotations;
    bool isDog = false;
    
};

// uint32_t - niezależnie od środowiska, zawsze 32 bitowa liczba nieujemna
// Definicja znajdujue się w pliku <stdint.h> dołączanym chociażby przez <string>

// Item - struktura reprezentująca pozycję zamówienia
// Definicja znajduje się w pliku <Item.hpp>

