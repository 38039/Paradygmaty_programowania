# Podaje indeks wybranej litery, jak jej nie ma zwróci -1

def podaj_indeks(napis, litera):
    indeks = -1
    for i, znak in enumerate(napis):
        if znak == litera: indeks = i
    return indeks