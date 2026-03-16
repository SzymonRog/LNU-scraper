#include "death_star_api.h"


void destroy_planet ( int max_imperator_anger )
{
    int anger = 0;
    do 
    {
        fire_ultimate_weapon();
        anger++;
        if(anger >= max_imperator_anger)
            break;
        
    }
    while (!is_planet_destroyed());
    
        
    
}
