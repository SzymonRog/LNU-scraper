def sumUp( args ):
    x = 1
    for i in range(len(args) + 1): 
        if i % 5 == 0: 
            if i == 5:
                args.insert(i, sum(args[i - 5 : i]) - min(args[i - 5 : i]) - max(args[i - 5 : i]))
            elif i != 0 :
                args.insert(i + x, sum(args[i + x - 5 : i + x]) - min(args[i + x - 5 : i + x]) - max(args[i + x - 5 : i + x]))
                x += 1    
    return args