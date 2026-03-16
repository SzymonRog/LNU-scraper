// Copyright (C) 2015-2016 Liga Niezwykłych Umysłów rev: 0.1
// This software is licensed under the LNU statements

#ifndef DEATH_STAR_API_H
#define DEATH_STAR_API_H

// is_planet_destroyed: Funkcja zwraca stan czy planeta została zniszczona
// Argumenty:
//      brak
// return:
//      bool:
//          true  - planeta została zniszczona
//          false - planeta jeszcze istnieje
bool is_planet_destroyed();

// fire_ultimate_weapon: Funkcja oddaje salwę z działa ostatecznego zniszczenia w kierunku planety
// Argumenty:
//      brak
// return:
//      brak
void fire_ultimate_weapon();

#endif // DEATH_STAR_API_H
