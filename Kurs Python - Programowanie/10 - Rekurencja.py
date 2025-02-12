# FUNKCJA LICZĄCA KWADRAT ARGUMENTU
def kwadrat(x): return x * x

# ZMIENNE W PYTHONIE MOGĄ PRZECHOWYWAĆ ZARÓWNO WARTOŚCI FUNKCJI
trzy_do_kwadratu = kwadrat(3)
print(trzy_do_kwadratu)

# JAK I SAME W SOBIE FUNKCJE
do_kwadratu = kwadrat
print(kwadrat(5))

# FUNKCJE MOGĄ BYĆ PRZEKAZYWANE JAKO ARGUMENTY FUNKCJI
def funkcja_uzytkownika(f1, c): return f1(c) + c

# KONSTRUKCJA FUNKCJI KWADRATOWEJ POPRZEZ ZDEFINIOWANIE WYRAZU WOLNEGO
# I JEJ POSTACI OGÓLNEJ PRZEZ KOLEJNĄ FUNKCJĘ LICZĄCĄ KWADRAT ARGUMENTU
print(funkcja_uzytkownika(kwadrat, 3))

# PRZYKŁAD REKURENCJI NA PODSTAWIE SILNI
def silnia(x):
    if x <= 1: return 1
    return x * silnia(x-1)

print(silnia(5))