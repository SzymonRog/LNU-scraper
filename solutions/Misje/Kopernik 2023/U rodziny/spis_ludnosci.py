def znajdz_rodzine( spis ):
    family = ['Barbara', 'Barbara', 'Mikołaj', 'Andrzej', 'Mikołaj', 'Katarzyna', 'Hohenzollern']
    index = 0
    for i in spis:
        if sorted(i) == sorted(family):
            break 
        else:
            index +=1 
            
    return index
    
    
        
    