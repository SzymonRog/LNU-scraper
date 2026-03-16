import time

def alarm_display(alarms, s12):
    for alarm in alarms:
       
        st = time.struct_time((
            alarm['Y'],     
            alarm['m'],     
            alarm['d'],     
            alarm['H'],     
            alarm['M'],     
            0,              
            0, 0, -1        
        ))

        if s12:
            # system 12h → %I (01–12) oraz %p (AM/PM)
            formatted = time.strftime("%Y-%m-%d %I:%M%p", st)
        else:
            # system 24h → %H (00–23)
            formatted = time.strftime("%Y-%m-%d %H:%M", st)

        print(formatted)
