// Zadanie:
// Na koniec 2005 roku PKB Grecji wynosił greece_gdp_2005. W kolejnych dziesięciu latach zmieniał się w następujący sposób:
// 1.   2006    +5.7 %
// 2.   2007    +3.3 %
// 3.   2008    -0.3 %
// 4.   2009    -4.3 %
// 5.   2010    -5.5 %
// 6.   2011    -9.1 %
// 7.   2012    -7.3 %
// 8.   2013    -3.2 %
// 9.   2014    +0.7 %
// 10. 2015    -0.2 %
// Uzupełnij funkcję calc_gdp_change w taki sposób, aby zwracała wartość PKB Grecji na koniec 2015 r. 

double calc_gdp_change( double greece_gdp_2005  )
{
    double rok_2015 = greece_gdp_2005;
    rok_2015 *= (1 + 57/1000.0);
    rok_2015 *= (1 + 33/1000.0);
    rok_2015 *= (1 - 3/1000.0);
    rok_2015 *= (1 - 43/1000.0);
    rok_2015 *= (1 - 55/1000.0);
    rok_2015 *= (1 - 91/1000.0);
    rok_2015 *= (1 - 73/1000.0);
    rok_2015 *= (1 - 32/1000.0);
    rok_2015 *= (1 + 7/1000.0);
    rok_2015 *= (1 - 2/1000.0);
    return rok_2015;
}
