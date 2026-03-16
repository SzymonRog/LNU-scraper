// Copyright (C) 2015-2016 Liga Niezwykłych Umysłów rev: 0.1
// This software is licensed under the LNU statements

#ifndef DRONE_H
#define DRONE_H

// get_speed: Funkcja zwraca aktualną prędkość opadania w m/s
// Argumenty:
//      brak
// return:
//      int: aktualna prędkość opadania w m/s
int get_speed();

// get_altitude: Funkcja zwraca aktualną wysokość w m
// Argumenty:
//      brak
// return:
//      int: aktualna wysokość w m
int get_altitude();

// get_rotations: Funkcja zwraca prędkość obrotową rotorów w obrotach / m
// Argumenty:
//      brak
// return:
//      int: aktualna prędkość obrotową rotorów w obrotach / m
int get_rotations();

// engines_on: Funkcja włącza silniki drona
// Argumenty:
//      brak
// return:
//      brak
void engines_on();

// engines_off: Funkcja wyłącza silniki drona
// Argumenty:
//      brak
// return:
//      brak
void engines_off();

#endif // DRONE_H
