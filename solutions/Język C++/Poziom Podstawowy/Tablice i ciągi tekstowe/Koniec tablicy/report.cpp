void report( unsigned short period_report[32] )
{
    int sum_prod = 0;
    for(int x = 0; x <=31; x++)
    {
        sum_prod += period_report[x];
    }
    period_report[31] = sum_prod;
}
