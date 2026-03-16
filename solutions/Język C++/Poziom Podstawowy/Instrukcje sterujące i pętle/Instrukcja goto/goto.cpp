int suma_wyrazow_ciagu ( int n )
{
    int suma = 0; 
    for (int i = 1; i <= n;i++)
    {
        suma += i*i;
    }
    
    return suma;
}