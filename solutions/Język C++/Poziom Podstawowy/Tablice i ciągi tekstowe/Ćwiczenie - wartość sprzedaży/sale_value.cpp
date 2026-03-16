float sale_value( float sale_april[31][2], float exchange[31] )
{
    float total_profit = 0;
    for (int i = 0; i <31;i++)
    {
        total_profit += (sale_april[i][0] * sale_april[i][1]) * exchange[i];
    }
    return total_profit;
}
