int calcDigitNumber( int digit, int number )
{
    int total_digit = 0;
    
     
    for(int i = 0; i <= number; i++)
    {
        int curr = i;
        while(curr > 0)
        {
            if( curr % 10 == digit )
                total_digit++;
            curr /= 10;
        }
    }
    return total_digit;
}
