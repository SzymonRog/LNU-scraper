// Copyright (C) 2015-2016 Liga Niezwykłych Umysłów rev: 0.1
// This software is licensed under the LNU statements

#ifndef LED_API_H
#define LED_API_H

// power_on: Funkcja zapala światło
// Argumenty:
//      brak
// return:
//      brak
void power_on(void);

// power_off: Funkcja gasi światło
// Argumenty:
//      brak
// return:
//      brak
void power_off(void);

// power_delay: Funkcja opóźnia wywołanie kolejnych funkcji API o [n] milisekund
// Argumenty:
//      ms: ilość milisekund opóźnienia
// return:
//      void: funkcja nie zwraca rezultatu
void power_delay( int time );

#endif // LED_API_H
