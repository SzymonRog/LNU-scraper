// Copyright (C) 2015-2016 Liga Niezwykłych Umysłów rev: 0.1
// This software is licensed under the LNU statements

#ifndef XORENCRYPT_H
#define XORENCRYPT_H

// send_message: funkcja wysyła zakryptowany tekst do serwera NSA
// Argumenty:
//      encrypted_text: zaszyfrowany tekst
// return:
//      void: funkcja nie zwraca rezultatu
void send_message( char encrypted_text[] );

#endif // XORENCRYPT_H
