#pragma once

#include <string>
#include <cstdint>

#include <OSqlQueryResult.hpp>
/* Klasa OSql::SqlQueryResult zawiera informacje o wyniku zapytania SQL.
 * Zawiera m. in. pola:
 * - data - dwuwymiarowa tablica std::string (czyli std::string**) reprezentująca pobrane dane
 *          data[x][y] - x - numer wiersza, y - numer kolumny
 * 
 * - rows - liczba wierszy
 * - columns - liczba kolumn
 * - status - status zapytania (Status::OK lub Status::ERROR)
 *  --------------------------------------------------------------------------------
 * Jest to bardzo uproszczona wersja 'takiej struktury'.
 * Wszystkie wiersze wynikowej tabeli pobierane są na raz do pamięci 
 * zarządzanej manualnie (tutaj przez resztę kodu, więc się o to nie martw)
 * W rzeczywistości wiersze powinny być pobierane dopiero gdy będą potrzebe i usuwane,
 * po wykonaniu pracy.
 * 
 * Takie funkcjonalności nie są jednak osiągalne dla 'zwykłej' struktury danych.
 */

namespace OSql
{
// Executes a query on the database
SqlQueryResult execQuery(const std::string& query);

}