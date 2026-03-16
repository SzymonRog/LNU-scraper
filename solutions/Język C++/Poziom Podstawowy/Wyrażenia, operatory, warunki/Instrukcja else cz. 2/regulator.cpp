
int temperature( int temp_actual, int temp_desired ) 
{
    if (temp_actual == temp_desired ) 
    return 0;
    else
        if ((abs(temp_desired - temp_actual)) <= 2) 
        return 1;
        else
            if ( abs(temp_desired - temp_actual) <= 5) 
            return 2;
            else
                if (abs(temp_desired - temp_actual) <= 10) 
                return 5;
                else
                    if ( abs(temp_desired  - temp_actual) <= 20) 
                    return 10;
                    else
                        if ( abs(temp_desired - temp_actual) > 20) 
                        return 20;
                        
}
