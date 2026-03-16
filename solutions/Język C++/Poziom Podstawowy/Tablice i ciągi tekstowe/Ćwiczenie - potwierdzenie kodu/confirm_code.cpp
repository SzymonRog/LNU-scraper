bool confirm_code ( char code_recieved[], char code_base[] )
{
    bool wynik = false;
    if(code_recieved == code_base) wynik = true;
    
    return wynik;
    
}
