int set_angle( unsigned short int counter )
{
    int kat = 0;
    int counter_1 = counter;
    switch(counter_1)
    {
        case 0: kat = 0;
            break;
        case 1: kat = 5;
            break;
        case 2: kat = 12;
            break;
        case 3: kat = 20;
            break;
        case 4: kat = 30; 
            break;
        case 5: kat = 45;
            break;
        case 6: kat = 60; 
            break;
        case 7: kat = 72;
            break;
        case 8: kat = 83; 
            break;
        case 9: kat = 90;
            default: kat = 90;
      
    }
    return kat;
}
