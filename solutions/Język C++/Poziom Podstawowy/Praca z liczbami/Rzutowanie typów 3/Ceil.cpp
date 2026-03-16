int Ceil( double value )
{
    int n = (int)value;
    if (value > 0 and value - n > 0)
        return n + 1;
    else if (value < 0 )
        return n;
    return n;
        
}
