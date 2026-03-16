from datetime import datetime

def wiek(krasnale):
    # Konwersja dat na obiekt datetime i wybór krasnala
    najstarszy_krasnal = min(
        krasnale,
        key=lambda krasnal: (datetime.strptime(krasnal['date'], '%d.%m.%Y'), krasnal['name'])
    )
    return najstarszy_krasnal['name']
            