int maxOpady(int tab[7], int pon, int wto, int sro, int czw, int pia, int sob, int nie){
    
    int max_rain = 0;
    int dni_opadow[7] = {pon , wto, sro, czw, pia, sob ,nie};
    for (int i = 0; i < 7; i++){
        
        tab[i] = dni_opadow[i];
        if(max_rain < dni_opadow[i]){
            max_rain = dni_opadow[i];
        } 
        
    }
    return  max_rain;
}