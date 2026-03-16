unsigned char turn_off_flag(unsigned char flags, int flag)
{
    unsigned int maska = 1;
    for(int i = 0; i < flag; i++)
    {
        maska *= 2;
    }
    int new_maska = 255 - maska; 
    flags &= new_maska;
    return flags;
}
