int calcSign(char text[], char sign)
{
    int counter = 0, i  = 0;
    while (text[i] != '\0')
    {
        if(text[i] == sign ) counter++ ;
        i++;
    }
    
    return counter;
}