// Zadanie:
// Ilu mieszkańców liczy w tym miejscu historii Daisy Town? Uzupełnij funkcję calcCitizens, aby jako wynik zwróciła tę wartość.

int calcCitizens( int totalCitizens )
{
    int members = (((((2 * totalCitizens) + 4) - 8) * 3) / 4) + 1;
    return members;
}
