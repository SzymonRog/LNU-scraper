from hidden_module import secret_task
import calendar
import time

def first_week_perf(year, month):
    weekday_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    month_calendar = calendar.monthcalendar(year, month)

    # szukamy pierwszego pełnego tygodnia
    first_full_week = None
    for week in month_calendar:
        if all(day != 0 for day in week):
            first_full_week = week
            break

    if first_full_week is None:
        return  # brak pełnego tygodnia w miesiącu

    for i, day in enumerate(first_full_week):
        start = time.time()
        secret_task(year, month, day)
        end = time.time()
        elapsed = end - start
        print(f"{day}, {weekday_names[i]}, {elapsed:.4f}s")
