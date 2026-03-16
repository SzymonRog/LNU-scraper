def disp_names( names ): 
    name_sorted = sorted(names, key=len)
    maxy = len(name_sorted[-1])
    for name1, name2 in zip(name_sorted, reversed(name_sorted)):
        print(f"{name1:^{maxy}}|{name2:^{maxy}}")