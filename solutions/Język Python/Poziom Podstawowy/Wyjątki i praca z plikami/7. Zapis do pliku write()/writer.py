#your code
file = open("prime_numbers.txt", "w")
x = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
for i in x:
    file.write(str(i) + "\n")
file.close()