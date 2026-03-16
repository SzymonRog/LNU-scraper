def kompresor( docelowe_cisnienie ):
 
    while zmierz_cisnienie() < docelowe_cisnienie:
        pompuj()
    
    
    