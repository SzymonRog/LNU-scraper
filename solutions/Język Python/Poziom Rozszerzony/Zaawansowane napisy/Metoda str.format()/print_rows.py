def print_rows(numbers):
    for i in range(0, len(numbers),2):
        pier = numbers[i]
        drug = numbers[i+1]
        print("{:<10.3%}{:.3%}".format(pier,drug))