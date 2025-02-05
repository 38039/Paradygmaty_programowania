# Wypisuje numer telefonu ze słownika za pomocą list comprehension

def wypisz_numer(kontakty):
    return [ telefon for (imie, nazwisko), telefon in kontakty.items if nazwisko == 'x' ]