#include "ventilation_api.h"

void emergency_ventilation ( void )
{
    int poziom_przed = get_ventilation_power();
    while(get_smoke_level() >= 450)
    {
        set_ventilation_power(100);
    }
    set_ventilation_power(poziom_przed);
}
