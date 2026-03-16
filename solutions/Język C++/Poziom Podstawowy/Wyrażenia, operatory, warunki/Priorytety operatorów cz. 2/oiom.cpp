// Zadanie
// Uzupełnij funkcję checkCondition() tak aby w przypadku przekroczenia którejkolwiek wartości zgłosiła prawidłowy alarm: WARNING, DANGER, CRITICAL.
// W przypadku gdyby wszystko było wporządku niech funkcja zgłosi wartość NORMAL.
#include<medical_api.h>
E_MEDICALS checkCondition()
{
    int sys    = get_systolic_pressure();
    int dia    = get_diastolic_pressure();
    int pulse  = get_pulse();
    float temp = get_temperature();
    int  stopnie = 0;
    
    if ((sys < 100 || sys > 139) || (dia < 70 || dia > 89)) stopnie += 1;
    if (pulse < 55 || pulse > 80) stopnie += 1;
    if(temp < 36.0 || temp > 37.0) stopnie += 1;
    
    if (stopnie == 1) return WARNING;
    if (stopnie == 2) return DANGER;
    if (stopnie >= 3) return CRITICAL;
return NORMAL;

    
}
