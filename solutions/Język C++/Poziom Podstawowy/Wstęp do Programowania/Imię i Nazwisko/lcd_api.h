// Copyright (C) 2015-2016 Liga Niezwykłych Umysłów rev: 0.1
// This software is licensed under the LNU statements

#ifndef LCD_API_H
#define LCD_API_H

// LCD_DELAY: stała oznaczająca ilość milisekund jaka musi upłynąć
//            między każdym poleceniem skierowanym do wyświetlacza LCD
//      wartość: 30 [ms]
#define LCD_DELAY 30

// LCD_LINE{N}: stała oznaczająca numer wiersza wyświetlacza LCD
//      wartość N: linia N-1
#define LCD_LINE1 0
#define LCD_LINE2 1
#define LCD_LINE3 2
#define LCD_LINE4 3
#define LCD_LINE5 4

// LCDDelay: Funkcja opóźnia wysyłanie komunikatu do wyświetlacza LCD
// Argumenty:
//      ms: ilość milisekund opóźnienia
// return:
//      void: funkcja nie zwraca rezultatu
void LCDDelay( unsigned int ms);

// LCDWriteChar: funkcja rysuje znak na ekranie wyświetlacza
//               w podanym wierszu i kolumnie
// Argumenty:
//      row: Numer wiersza zaczynający się od indeksu 0 np. LCD_LINE1
//      col: Numer kolumny zaczynający się od indeksu 0, max col = 15
//      character: znak wysłany na ekran wyświetlacza LCD
// Zwraca:
//      void: funkcja nie zwraca rezultatu
void LCDWriteChar( unsigned int row, unsigned int col, const char character );

// LCDWriteString: funkcja rysuje napisy na ekranie wyświetlacza
// Argumenty:
//      line1: łańcuch tekstowych typu (char *)
//      line2: łańcuch tekstowych typu (char *)
// Zwraca:
//      void: funkcja nie zwraca rezultatu
void LCDWriteString( const char * line1, const char * line2 );

// LCDInit: Funkcja inicjuje wyświetlacz, czyści jego zawartość
// Argumenty:
//      void: funkcja nie pobiera argumentów
// return:
//      void: funkcja nie zwraca rezultatu
void LCDInit(void);

#endif // LCD_API_H
