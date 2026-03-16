from datetime import datetime, date, time, timedelta

def flight_postpone(dates, times):
    now = datetime.now()
    flights = []
    free_dates = set()
    
    for i in range(len(dates)):
        if times[i]:
            flight_datetime = datetime.combine(dates[i], times[i])
            flights.append(flight_datetime)
        else:
            if dates[i] >= now.date():
                free_dates.add(dates[i])
    
    flights.sort()
    
    postponed_flights = []
    used_times = {}
    
    for flight in flights:
        if flight < now:
            if free_dates:
                new_date = free_dates.pop()
                new_time = flight.time()
                
                if new_date not in used_times:
                    used_times[new_date] = set()
                
                while new_time in used_times[new_date]:
                    new_time = (datetime.combine(date.today(), new_time) + timedelta(hours=1)).time()
                
                new_flight = datetime.combine(new_date, new_time)
                used_times[new_date].add(new_time)
                postponed_flights.append(new_flight)
            else:
                new_flight = flight + timedelta(days=1)
                while new_flight.date() in used_times:
                    new_flight += timedelta(days=1)
                
                if new_flight.date() not in used_times:
                    used_times[new_flight.date()] = set()
                
                used_times[new_flight.date()].add(new_flight.time())
                postponed_flights.append(new_flight)
        else:
            postponed_flights.append(flight)
            if flight.date() not in used_times:
                used_times[flight.date()] = set()
            used_times[flight.date()].add(flight.time())
    
    return postponed_flights