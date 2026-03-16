// Copyright (C) 2015-2016 Liga Niezwykłych Umysłów rev: 0.1
// This software is licensed under the LNU statements

#ifndef EMPTY_BLOCKS_H
#define EMPTY_BLOCKS_H

// get_content: Funkcja zwraca czy klocek o współrzędnych x,y,z jest wypełniony
// Argumenty:
//      x: pozycja x klocka
//      y: pozycja y klocka
//      z: pozycja z klocka
// return:
//      bool:
//           true  - jesli klocek jest wypełniony
//           false - jesli klocek jest pusty
bool get_content ( int x, int y, int z );

#endif // EMPTY_BLOCKS_H
