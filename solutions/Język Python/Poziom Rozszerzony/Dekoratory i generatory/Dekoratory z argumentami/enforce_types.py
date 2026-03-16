import this
def enforce_types(t1, t2):
    
    def decorator(funkcja):
        
        def inner(a1, a2):
            if  type(a1) == t1 and type(a2) == t2:
                return funkcja(a1, a2)
            else:
                raise TypeError
                
        return  inner
    return decorator
            









@enforce_types(int, int)
# /* read-only */
def add_ints(x, y):
    return x + y
# /* read-only */
@enforce_types(str, str)
# /* read-only */
def concat_strings(s1, s2):
    return s1 + s2
# /* read-only */
