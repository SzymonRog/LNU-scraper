def rhymeList( words ):
    reverse_list = []
    for i in words:
        reverse_list.append(i[::-1])
        
    rymy_reverse = sorted(reverse_list)
    rymy = []
    
    for i in rymy_reverse:
        rymy.append(i[::-1])
        
    return rymy
        
        