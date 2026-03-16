
import math
def format():
    
    file1 = open("preData.txt", "r+")
    file2 = open("data.txt", "w+")
    
    x = []
    j = 0
    
    
    for i in file1:
        x.append(i)
        
    for i in x:
        x[j] = x[j][0:2]
        j += 1
        
    for i in x:
        file2.write( i + " " + str(math.sqrt(int(i))) + "\n" )
    
    
    file1.close()
    file2.close()
