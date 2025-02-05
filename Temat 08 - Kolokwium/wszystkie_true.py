# Wszystkie wartości true albo zwraca false

def wszystkie_true(tablica):
    for wartosc in tablica:
        if not wartosc:
            return False
    return True