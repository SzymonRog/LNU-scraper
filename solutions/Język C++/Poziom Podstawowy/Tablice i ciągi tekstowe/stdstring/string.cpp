#include <iostream>
#include <string>

void klasa_std_string()
{
    // Tworzenie ciągu tekstowego z inicjalizacją
    std::string str1 ("Ala ma kota");

    // Wyświetlanie na ekranie
    std::cout << "str1 = " << str1 << std::endl;

    // Tworzenie drugiego ciągu tekstowego:
    std::string str2;

    // Przypisanie jednego ciągu do drugiego
    str2 = str1;

    // Wyświetlenie drugiego ciągu po operacji przypisania:
    std::cout << "str2 po przypisaniu = " << str2 << std::endl;

    // Zmiana wartości pierwszego ciągu tekstowego
    str1 = ", a kot ";

    // Dopisanie do pierwszego ciągu kolejnego łańcucha
    str1 += "ma Alę";

     // Wyświetlanie pierwszego ciągu po zmianie wartości
    std::cout << "str1 po zmianie = " << str1 << std::endl;

    //Tworzenie trzeciego ciągu tekstowego
    std::string addStr;

    //Przypisanie trzeciemu ciągowi sumy dwóch pierwszych
    addStr = str2 + str1;

    //Wyświetlenie wyniku dodania dwóch ciągów:
    std::cout << "str2 + str1 = " << addStr << std::endl;
}
