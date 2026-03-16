def generateBilling(x):
    file = open("billing.txt", "w")
    for i in x:
        file.write(i[0] + ", " + i[1] + ", " + i[2] + "\n")
    file.close()
  