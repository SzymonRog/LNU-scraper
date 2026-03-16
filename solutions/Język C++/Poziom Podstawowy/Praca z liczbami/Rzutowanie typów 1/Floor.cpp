int Floor( double value )
{
    if (value < 0 and value - (int)value < 0) return (int)value - 1;
    return (int)value;
}
