// Copyright (C) 2019 Liga Niezwykłych Umysłów rev: 0.1
// This software is licensed under the LNU statements

#ifndef HACKASHAQ_H
#define HACKASHAQ_H

// test_pass: Funkcja sprawdza czy dany znak znajduje się w haśle na podanym miejscu
// Argumenty:
//      position:   zmienna typu int okreslajaca numer sprawdzanego miejsca w haśle, 
//                  zmienna przyjmuje wartości od 0 do 15
//      value:      zmienna typu char przechowująca sprawdzaną wartość
// return:
//      funkcja zwraca wartość true, jeżeli w haśle na miejscu określonym przez posiotion 
//      znajduje się znak przypisany do value
bool test_pass( int position, char value );

// confirm: Funkcja przesyła na serwer i zatwierdza hasło zapisne w 16-elementowej tablicy typu char
// Argumenty:
//      password[16] szesnastoelementowa tablica typu char
// return:
//      brak
void confirm( char password[] );

#endif // HACKASHAQ_H
