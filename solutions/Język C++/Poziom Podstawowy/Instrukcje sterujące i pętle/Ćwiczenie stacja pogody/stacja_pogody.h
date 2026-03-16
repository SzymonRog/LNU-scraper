// Copyright (C) 2015-2016 Liga Niezwykłych Umysłów rev: 0.1
// This software is licensed under the LNU statements

#ifndef STACJA_POGODY_H
#define STACJA_POGODY_H

// get_temp: Funkcja zwraca temperature w stopniach Celsjusza dla podanej godziny, dnia, miesiąca, roku
// Argumenty:
//      hour : godzina <0-23>
//      day  : dzien <1-31>
//      month: miesiąc <1-12>
//      year : rok <1980-2015>
// return:
//      int: temperatura w stopniach Celsjusza
// error: -99
//      w przypadku błedu (np zła data)
int get_temp( int hour, int day, int month, int year );

#endif // STACJA_POGODY_H
