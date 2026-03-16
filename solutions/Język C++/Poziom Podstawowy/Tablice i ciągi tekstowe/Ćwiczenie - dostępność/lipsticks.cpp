unsigned int check_availability ( unsigned char lipsticks_in_store[25][2], unsigned char article )
{
    int stan = 0;
    for (int i = 0;i < 25;i++)
    {
        if(lipsticks_in_store[i][0] == article) stan  =  lipsticks_in_store[i] [1];
    }
    return stan;
}
