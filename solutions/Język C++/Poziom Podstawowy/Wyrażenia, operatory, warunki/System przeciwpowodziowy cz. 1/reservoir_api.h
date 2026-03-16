// Copyright (C) 2015-2016 Liga Niezwykłych Umysłów rev: 0.1
// This software is licensed under the LNU statements

#ifndef RESERVOIR_API_H
#define RESERVOIR_API_H

// Lista nazw zbiorników i ich punktów kontrolnych
enum E_RESERVOIRS
{
    POLDER_UNKNOWN = 0,
    POLDER_BUKOW,
    POLDER_KRZESIN,
    POLDER_KOZLE,
    POLDER_OBROWIEC,
    POLDER_OPOLE,
    POLDER_ZELAZNA
};

// getCapacity: funkcja zwraca objętność zbiornika w m3 dla zadanego punktu E_RESERVOIRS
// Argumenty:
//      reservoirs: zmienna typu E_RESERVOIRS opisująca punkt pomiarowy
// return:
//      int: objętość zbiornika reservoirs w m3.
//           tożsame z getLength( reservoir ) * getWidth( reservoir ) * getDepth( reservoir )
int getCapacity( E_RESERVOIRS reservoirs );

// getLevel: funkcja zwraca aktualny poziom wody w zbiorniku w m
// Argumenty:
//      reservoirs: zmienna typu E_RESERVOIRS opisująca punkt pomiarowy
// return:
//      int: poziom wody w m w zbiorniku reservoir
int getLevel( E_RESERVOIRS reservoirs );

// getLength: funkcja zwraca długość zbiornika w m
// Argumenty:
//      reservoirs: zmienna typu E_RESERVOIRS opisująca punkt pomiarowy
// return:
//      int: długość zbiornika w m
int getLength( E_RESERVOIRS reservoirs );

// getWidth: funkcja zwraca szerokość zbiornika w m
// Argumenty:
//      reservoirs: zmienna typu E_RESERVOIRS opisująca punkt pomiarowy
// return:
//      int: szerokość zbiornika w m
int getWidth( E_RESERVOIRS reservoirs );

// getDepth: funkcja zwraca głębokość zbiornika w m
// Argumenty:
//      reservoirs: zmienna typu E_RESERVOIRS opisująca punkt pomiarowy
// return:
//      int: głębokość zbiornika w m
int getDepth( E_RESERVOIRS reservoirs );

// getWidth: funkcja zwraca szerokość rzeki w m
// Argumenty:
//      reservoirs: zmienna typu E_RESERVOIRS opisująca punkt pomiarowy
// return:
//      int: szerokość rzeki w m
int getRiverWidth( E_RESERVOIRS reservoirs );

// getRiverSpeed: funkcja zwraca prędkość rzeki w m/s w punkcie pomiarowym
// Argumenty:
//      reservoirs: zmienna typu E_RESERVOIRS opisująca punkt pomiarowy
// return:
//      int: prędkość rzeki w m/s
int getRiverSpeed( E_RESERVOIRS reservoirs );

// getRiverLevel: funkcja zwraca aktualny poziom wody w rzece w m
// Argumenty:
//      reservoirs: zmienna typu E_RESERVOIRS opisująca punkt pomiarowy
// return:
//      int: poziom wody w m w rzece
int getRiverLevel( E_RESERVOIRS reservoirs );

#endif // RESERVOIR_API_H
