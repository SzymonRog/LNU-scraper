def setPower(pm25, pm10):
    # określenie indeksu dla PM2.5
    if pm25 <= 12:
        index25 = 0
    elif pm25 <= 24:
        index25 = 1
    elif pm25 <= 36:
        index25 = 2
    else:
        index25 = 3

    # określenie indeksu dla PM10
    if pm10 <= 20:
        index10 = 0
    elif pm10 <= 50:
        index10 = 1
    elif pm10 <= 80:
        index10 = 2
    else:
        index10 = 3

    # zwracamy gorszy (większy) indeks
    return max(index25, index10)
