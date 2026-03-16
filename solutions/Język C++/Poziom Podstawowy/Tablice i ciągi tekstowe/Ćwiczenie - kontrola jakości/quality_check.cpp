unsigned int quality_report( bool quality_check[1000] )
{
    int wada = 0;
    for(int x = 0;x < 1000;x++)
    {
        if(!(quality_check[x])) wada += 1;
    }
    
    return wada;
}
