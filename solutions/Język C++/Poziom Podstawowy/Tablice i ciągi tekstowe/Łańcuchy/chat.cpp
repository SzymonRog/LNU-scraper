int available_length( char str[], int max_length )
{
    int i = 0;
    while(1)
    {
        if(str[i] == '\0') break;
        i++;
    }
    
    if(max_length < i) return -1;
    return max_length - i;
}
