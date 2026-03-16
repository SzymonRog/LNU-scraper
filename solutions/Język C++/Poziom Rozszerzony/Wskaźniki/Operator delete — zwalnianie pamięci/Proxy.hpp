#pragma once

#include <ProductId.hpp>

#include <string>

/// @brief Zwróci tablicę zawierającą id wszystkich produktów w danej kategorii
/// @param category Wskaźnik na nazwę kategorii
/// @param numberOfProducts Liczba pod przekazanym adresem
///        zostanie ustawiona na długość zwracanej tablicy
/// @return Wskaźnik na (nowo ulokowaną) tablicę zawierającą id produktów
ProductId* getProductIds(std::string* category, unsigned int* numberOfProducts);

/// @param productId Id produktu
/// @return Cena przekazanego produktu
unsigned int getProductPrice(ProductId* productId);

/// @param productId Id produktu
/// @return Ilość produktu w magazynie
unsigned int getProductQuantity(ProductId* productId);
