#Tu zaimportuj moduł time
import time

def sleepy_years(sleep_time):
    time.sleep(2 * sleep_time) 
    return time.time() / 3600 