int estimate_victims( unsigned short int imperator_anger )
{
    int ofiary = 0;
    int anger = imperator_anger;
    switch(anger)
    {
        case 0:ofiary = 100;
            break;
        case 1:ofiary = 1000;
            break;
        case 2:ofiary = 5000;
            break;
        case 3:ofiary = 10000;
            break;
        default: ofiary = 10000000;
            
    }
    return ofiary;
}
