def avgParticles( file ):
    try:
        f = open(file, 'r')
        x = f.readlines()
    except:
        return "file not found"
    w = 0 
    s = 0 
    try:
        for i in x:
            s += float(i)
            w += 1
        return  float(s / w)
    except:
            return "wrong data"
    
        

