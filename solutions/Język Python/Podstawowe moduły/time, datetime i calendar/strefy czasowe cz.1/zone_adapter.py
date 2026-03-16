import os, time, calendar

def zone_adapter(st, zone_list):
    diff = (calendar.timegm(st) - calendar.timegm(time.gmtime())) // 3600
    timezone = zone_list[diff + 12]

    os.environ['TZ'] = f'{timezone}{-diff:+03d}'
    time.tzset()