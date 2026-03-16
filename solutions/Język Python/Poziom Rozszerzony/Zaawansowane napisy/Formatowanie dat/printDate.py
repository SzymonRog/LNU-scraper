import datetime
def printDate( year, month, day ):
    date = datetime.datetime(year, month, day)
    print(f"Date: {date:%Y-%m-%d}")