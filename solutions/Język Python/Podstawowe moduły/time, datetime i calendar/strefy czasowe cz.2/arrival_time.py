import datetime

def arrival_time(dt, duration, direction):
    utc_offset = dt.utcoffset()
    
    if direction == 'e':
        return (dt + duration + utc_offset).astimezone(datetime.UTC)
    elif direction == 'w':
        return (dt + duration - utc_offset).astimezone(datetime.UTC)