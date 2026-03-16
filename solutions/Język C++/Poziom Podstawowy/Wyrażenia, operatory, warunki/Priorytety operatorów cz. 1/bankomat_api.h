// Copyright (C) 2015-2016 Liga Niezwykłych Umysłów rev: 0.1
// This software is licensed under the LNU statements

#ifndef BANKOMAT_API_H
#define BANKOMAT_API_H

// E_BANKI: wartość wyliczeniowa, numer banku kontrolowany przez Ligowa Inspekcje Bankowa
//      BANK = {numer}
enum E_BANKI
{
    BANK_POLSKI         = 1,
    BANK_LNU            = 2,
    BANK_ROBOTOW        = 3
};

// E_NOMINALY: wartość wyliczeniowa, nominaly platnicze
//      NOMINAL = {wartosc}
enum E_NOMINALY
{
    NOMINAL_50          = 50,
    NOMINAL_100         = 100,
    NOMINAL_200         = 200
};

// getBanknoty: Funkcja zwraca ilość dostępnych banknotów w podanym banku dla zadanego nominału
// Argumenty:
//      bank: numer banku, wartosc typu E_BANKI
//      nominal: wartość nominału tupu E_NOMINALY
// return:
//      int: ilość banknotów w danym banku dla zadanego nominału
int getBanknoty( E_BANKI bank, E_NOMINALY nominal );

#endif // BANKOMAT_API_H
