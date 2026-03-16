def add6months( date ):
    rok = int(date[:4])
    miesac = int(date[5:])
    if miesac > 6:
        miesac = (miesac + 6) % 12
        rok += 1
    else:
        miesac += 6
    miesac = str(miesac)
    rok = str(rok)
    if len(miesac) == 1:
        miesac  = "0" + miesac
    return rok +  "." + miesac
        
        
        