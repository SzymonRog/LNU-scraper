import datetime

def flight_delay(dt: datetime.datetime):
    # aktualny czas z użyciem isoformat()
    now = datetime.datetime.fromisoformat(datetime.datetime.now().isoformat())
    
    if now <= dt:
        return 0, 0  # brak opóźnienia
    
    delay = now - dt
    seconds = delay.seconds

    hours = seconds // 3600
    minutes = (seconds % 3600) // 60

    return f"0{hours}:{minutes}"
