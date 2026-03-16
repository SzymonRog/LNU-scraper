import calendar

def unlucky_range(year, year_range):
    max_count = 0
    unlucky_years = []

    # wliczamy rok końcowy w przedziale (year + year_range włącznie)
    for y in range(year, year + year_range + 1):
        count = 0
        for m in range(1, 13):
            if calendar.weekday(y, m, 13) == 4:  # piątek = 4
                count += 1

        if count > max_count:
            max_count = count
            unlucky_years = [y]
        elif count == max_count:
            unlucky_years.append(y)

    return unlucky_years
