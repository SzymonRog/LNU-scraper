import calendar

def date_display(year, month, day):
    # nazwa dnia tygodnia (0 = Monday)
    weekday_name = calendar.day_name[calendar.weekday(year, month, day)]
    
    # nazwa miesiąca (1 = January)
    month_name = calendar.month_name[month]
    
    return f"{weekday_name} {day} {month_name} {year}"
