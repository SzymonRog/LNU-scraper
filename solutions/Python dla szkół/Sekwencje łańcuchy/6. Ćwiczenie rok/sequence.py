def get_year( year ):
    if year[0] == "_":
        return year[1:]
    else:
        return year[:-1]