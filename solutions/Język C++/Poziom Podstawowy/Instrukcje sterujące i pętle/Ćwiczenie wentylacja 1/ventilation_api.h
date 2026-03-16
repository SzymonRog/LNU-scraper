// Copyright (C) 2015-2016 Liga Niezwykłych Umysłów rev: 0.1
// This software is licensed under the LNU statements

#ifndef VENTILATION_API_H
#define VENTILATION_API_H

// SMOKE_ALARM jest stałą określającą alarmowy poziom zadymienia powietrza w mg/m3
#define SMOKE_ALARM     450

// get_smoke_level: Funkcja zwraca aktualny poziom zadymienia w mg/m3
// Argumenty:
//      brak
// return:
//      int: poziom zadymienia w mg/m3
int get_smoke_level( void );

// get_ventilation_power: Funkcja zwraca moc silników wentylatora w %
// Argumenty:
//      brak
// return:
//      power: procentowo moc silnika <0,100> %
int get_ventilation_power( void );

// set_ventilation_power: Funkcja ustawia silniki wentylatora na moc = power
// Argumenty:
//      power: procentowo moc silnika <0,100> %
// return:
//      brak
void set_ventilation_power( int power );

#endif // VENTILATION_API_H
