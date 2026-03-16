import calendar

def month_guesser(year, first_weekday, days):
    months = list(calendar.month_name)[1:]
    matching_months = []
    for month in range(1, 13):
        month_days, month_start_weekday = calendar.monthrange(year, month)[1], calendar.monthrange(year, month)[0]
        if ((first_weekday is None or month_start_weekday == first_weekday) and
            (days is None or month_days == days)):
            matching_months.append(months[month - 1])
    if matching_months:
        for m in matching_months:
            print(m)
    else:
        print("None")
