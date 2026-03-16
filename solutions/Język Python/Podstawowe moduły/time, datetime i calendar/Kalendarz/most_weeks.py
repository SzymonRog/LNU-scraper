import calendar

def most_weeks(year, month_names):
    c = calendar.Calendar()
    months = []
    res = []
    for row in c.yeardayscalendar(year):
        for month in row:
            months.append(len(month))
    for index, weeks in enumerate(months):
        if weeks == max(months):
            res.append(month_names[index])
    return res
