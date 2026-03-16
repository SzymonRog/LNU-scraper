import time

def age_struct(st, t):
   
    original_ts = time.mktime(st)

    new_ts = original_ts + t

    
    if new_ts < 0:
        new_ts = 0

    
    new_st = time.localtime(new_ts)

    
    return (new_st.tm_year, new_st.tm_mon, new_st.tm_mday)
