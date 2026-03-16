import datetime

def desc_offset(dts):
    unique_timezones = dict.fromkeys(sorted([dt.tzinfo for dt in dts], key=str))

    for tz in unique_timezones:
        now = datetime.datetime.now(tz)
        utc_offset = now.utcoffset().total_seconds() / 3600
        print(f"{tz}, {utc_offset:+.1f}")