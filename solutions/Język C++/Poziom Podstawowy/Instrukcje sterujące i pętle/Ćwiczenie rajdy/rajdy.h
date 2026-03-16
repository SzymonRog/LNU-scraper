// Copyright (C) 2015-2016 Liga Niezwykłych Umysłów rev: 0.1
// This software is licensed under the LNU statements

#ifndef RAJDY_H
#define RAJDY_H

// get_time: Funkcja zwraca czas w sekundach pokonania przez samochód odcinka o numerze check_point
// Argumenty:
//      check_point: numer odcinka
// return:
//      int: czas w sekundach
int get_time( int check_point );

// get_lenght: Funkcja zwraca długość w metrach odcinka o numerze check_point
// Argumenty:
//      check_point: numer odcinka
// return:
//      int: długość w metrach
int get_length( int check_point );

#endif // RAJDY_H
