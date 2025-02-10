# Napisz funkcję sumuj_napisy, która może przyjmować
# dowolną liczbę par napisów (np. ("Jan", "Nowak"))
# i zwracać listę połączonych napisów.

def sumuj_napisy(*napisy):
    return [f"{imie}{nazwisko}" for imie, nazwisko in napisy]