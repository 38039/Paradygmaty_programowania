# DEKLARACJA SŁOWNIKA
slownik = {
    1 : "Poniedziałek",
    2 : "Wtorek",
    3 : 5
}

# OCZYT SŁOWNIKA
print(slownik)

# ODCZYT WARTOŚCI SŁOWNIKA (PRZEZ INEKS)
print(slownik[3])

# NADPISANIE WARTOŚCI SŁOWNIKA
slownik[3] = "Środa"
print(slownik)

# WYJŚCIE POZA ZAKRES SŁOWNIKA
# SKUTKUJE WYRZUCENIEM WYJĄTKU: KeyError

# METODA ZWRACAJĄCA WARTOŚĆ GDY INDEKS SŁOWNIKA NIE ZOSTANIE ODNALEZIONY
print(slownik.get(4, "KeyError"))

# DOMYŚLNIE FOR ITERUJE PO KLUCZACH SŁOWNIKA (NIE WARTOŚCIACH)
for key in slownik:
    print(key)

# METODA UMOŻLIWIAJĄCA ITERACJE PO WARTOŚCIACH SŁOWNIKA
for value in slownik.values():
    print(value)

# METODA DO USUWANIA WARTOŚCI ZE SŁOWNIKA
slownik.pop(1)
print(slownik)