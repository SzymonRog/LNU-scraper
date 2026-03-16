// Copyright (C) 2015-2016 Liga Niezwykłych Umysłów rev: 0.1
// This software is licensed under the LNU statements

#ifndef ALPR_API_H
#define ALPR_API_H

// ALPR API = Automatic License Plate Recognition API
// Zbiór narzędzi programistycznych do optycznej kontroli tablic rejestracyjnych pojazdów

// get_license_number: Funkcja zwraca liczbowy numer rejestracyjny (np. dla rejestracji "DW 00001" zwraca numer 1)
// Argumenty:
//      brak
// return:
//      int: liczbowy numer rejestracyjny
int get_license_number(void);

// get_day_of_month: Funkcja zwraca numer dnia miesiąca (np. dla daty (21/04/2016 zwróci numer 21)
// Argumenty:
//      brak
// return:
//      int: numer dnia miesiąca
int get_day_of_month(void);

// get_current_speed: Funkcja zwraca aktualną prędkość w km/h (np. 60 = 60km/h)
// Argumenty:
//      brak
// return:
//      int: prędkość w km/h
int get_current_speed(void);

#endif // ALPR_API_H