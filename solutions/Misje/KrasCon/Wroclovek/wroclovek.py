#python

def reszta(zaplacona_kwota, ilosc_magnesow, ilosc_dlugopisow, ilosc_pocztowek, ilosc_figurek):
    sum_mag = round(ilosc_magnesow * 5.40,2)
    sum_dlug = round(ilosc_dlugopisow * 3.49,2)
    sum_poczt = round(ilosc_pocztowek * 2.99,2)
    sum_figu = round(ilosc_figurek * 10.35,2)
    
    koszt = sum_mag +  sum_dlug + sum_poczt + sum_figu 
    
    if koszt > zaplacona_kwota:
        return "Złodziej"
    else:
        return round(zaplacona_kwota - koszt,2)