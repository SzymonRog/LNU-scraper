// Copyright (C) 2015-2016 Liga Niezwykłych Umysłów rev: 0.1
// This software is licensed under the LNU statements

#ifndef LED_API_H
#define LED_API_H

// DELAY_DOT:   stała w [ms] definiująca krótki sygnał świetlny
//              odpowiadający "kropce" według alfabetu Morse'a
//      wartość: 30 [ms]
#define DELAY_DOT       30

// DELAY_DASH:  stała w [ms] definiująca długi sygnał świetlny
//              odpowiadający "kresce" według alfabetu Morse'a
//      wartość: 90 [ms]
#define DELAY_DASH      90

// DELAY_NEXT:  stała w [ms] definiująca odstęp między elementami znaku
//              według alfabetu Morse'a
//      wartość: 30 [ms]
#define DELAY_NEXT      30

// DELAY_SPACE: stała w [ms] definiująca odstęp między znakami
//              według alfabetu Morse'a
//      wartość: 90 [ms]
#define DELAY_SPACE     90

// power_on: Funkcja zapala diodę LED
// Argumenty:
//      brak
// return:
//      brak
void power_on(void);

// power_off: Funkcja gasi diodę LED
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
