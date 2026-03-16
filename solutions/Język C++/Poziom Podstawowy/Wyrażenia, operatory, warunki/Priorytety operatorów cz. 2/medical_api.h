// Copyright (C) 2015-2016 Liga Niezwykłych Umysłów rev: 0.1
// This software is licensed under the LNU statements

#ifndef MEDICAL_API_H
#define MEDICAL_API_H

// Lista stanów alarmowych
enum E_MEDICALS
{
    UNKNOWN = 0,
    NORMAL,
    WARNING,
    DANGER,
    CRITICAL
};

// get_systolic_pressure: funkcja zwraca ciśnienie skurczowe podłączonego pacjenta
// Argumenty:
//      brak: funkcja nie pobiera żadnych wartości
// return:
//      int: ciśnienie skurczowe
int get_systolic_pressure();

// get_diastolic_pressure: funkcja zwraca ciśnienie rozkurczowe podłączonego pacjenta
// Argumenty:
//      brak: funkcja nie pobiera żadnych wartości
// return:
//      int: ciśnienie rozkurczowe
int get_diastolic_pressure();

// get_pulse: funkcja zwraca ilość uderzeń serca na minute podłączonego pacjenta
// Argumenty:
//      brak: funkcja nie pobiera żadnych wartości
// return:
//      int: ilość uderzeń serca na minute
int get_pulse();

// get_temperature: funkcja zwraca temperature ciała w stopniach celcjusza podłączonego pacjenta
// Argumenty:
//      brak: funkcja nie pobiera żadnych wartości
// return:
//      int: temperatura w stopniach celcjusza
float get_temperature();

#endif // MEDICAL_API_H
