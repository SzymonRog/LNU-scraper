import math

def anagrams(x):
    l_kombinacji = 1
    n = len(x)
    word = []
    word_number = []
    for i in x:
        if i not in word:
            word.append(i)
            word_number.append(x.count(i))
               
               
               
               
    for i in word_number:
        l_kombinacji *= math.comb(n,i)
        n -= i
            
            
            
    return l_kombinacji
           
       