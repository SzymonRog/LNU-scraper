// Copyright (C) 2015-2016 Liga Niezwykłych Umysłów rev: 0.1
// This software is licensed under the LNU statements

#ifndef PARKING_API_H
#define PARKING_API_H

// get_range: Funkcja zwraca odległość w [cm] między dalmierzem a przeszkodą
// Argumenty:
//      floor: numer piętra
//      place: numer miejsca parkingowego
// return:
//      int: zwraca ilość cm od przeszkody
// error:
//      w przypadku błędu pomiaru funkcja zwraca wartość -1
int get_range( int floor, int place );

#endif // PARKING_API_H
