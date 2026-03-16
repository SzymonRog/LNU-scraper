import calendar

lhc = calendar.LocaleHTMLCalendar(locale='fr_FR.UTF-8')
        
with open("index.html", "w", encoding="utf-8") as file:
    file.write(lhc.formatyear(2024))