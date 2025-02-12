# ZADANIE 2: WARIANCJA
#
# Należy napisać JEDNĄ funkcję liczącą  średnią wartości z tablicy (x) oraz ich wariancję (w) wg wzorów:
# Wzór na Wariancje
# Wzór na Średnią
# gdzie N-liczba elementów tablicy, xi - i-ty element tablicy.  Proszę tu wykorzystać dwie pętle for (nie używać np. sum)
#
# Funkcja ma otrzymywać tablicę jako argument i zwracać OBIE obliczone wartości (ale nie w postaci słownika).
# Następnie napisz program, w którym do tablicy (listy) wpisywane są liczby z klawiatury - zacznij od pustej listy i dokładaj do niej elementy za pomocą append. Niech wpisanie 0 kończy dokładanie. Wywołaj napisaną funkcję z tą tablicą i wypisz uzyskane wyniki w DWÓCH osobnych liniach:
# Średnia wynosi: ...
#
# Wariancja wynosi: ...
# Następnie jeszcze dwukrotnie wywołaj napisaną funkcję z tablicami [3,3,3,3] oraz [5,6,7,8,9] i ponownie wypisz uzyskane wyniki

def obliczenia(tab):
    suma = 0
    for x in tab: suma += x
    srednia = suma / len(tab)

    suma = 0
    for xi in tab: suma += (xi - srednia) ** 2
    wariancja = suma / len(tab)

    return srednia, wariancja


tab1 = [3, 3, 3, 3]
srednia, wariancja = obliczenia(tab1)
print(f"Srednia wynosi = {srednia}")
print(f"Wariancja wynosi = {wariancja}")

tab2 = [5, 6, 7, 8, 9]
srednia, wariancja = obliczenia(tab2)
print(f"Srednia wynosi = {srednia}")
print(f"Wariancja wynosi = {wariancja}")

lst = []
while (True):
    x = int(input('Enter a number: '))
    if x == 0: break
    lst.append(x)

srednia, wariancja = obliczenia(lst)
print(f"Srednia wynosi = {srednia}")
print(f"Wariancja wynosi = {wariancja}")