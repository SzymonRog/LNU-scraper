# Your code goes here
def censor(func, *args , **kwarq):
    new_args = [i for i in args if  "k" not in str(i)]
    new_kwarq = dict((x, y) for x, y in [i for i in kwarq.items() if "k" not in str(i)])
    return func(*new_args,**new_kwarq)
    
   
    