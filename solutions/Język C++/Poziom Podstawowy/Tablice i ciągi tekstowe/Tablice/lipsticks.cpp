unsigned int lipsticks_per_month( unsigned short lipsticks_per_day[] )
{
    int sum_prod = 0;
    for(int x = 0; x <=31; x++)
    {
        sum_prod += lipsticks_per_day[x];
    }
    
    return sum_prod;
}