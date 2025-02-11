# STRUKTURA DANYCH: TABLICA (C, C++)
# - PRZECHOWUJE WARTOŚCI TEGO SAMEGO TYPU
# - WSZYSTKIE ELEMENTY SĄ INDEKSOWANE PRZEZ ADRES W PAMIĘCI
# - ILOŚĆ ELEMENTÓW TABLICY MUSI BYĆ ZDEFINIOWANA
# - MOŻLIWOŚĆ MANIPULACJI ELEMENTAMI TABLICY
# - ZAWSZE SKOŃCZONA, ILOŚĆ ELEMENTÓW MUSI BYĆ PREDEFINIOWANA

# Definicja tablicy w C
# int tablica[5] = [1, 2, 3, 4, 5];
# Typ danych:         int
# Ilość elementów:    [5]
# Wartości elementów: [1, 2, 3, 4, 5]

# Interpretacja graficzna tablicy
# Zawartość: [1]   [2]   [3]   [4]   [5]
# Indeks:     0     1     2     3     4
# Adres:      0x100 0x104 0x108 0x10C 0x110


# STRUKTURA DANYCH: LISTA (JAVA, PYTHON)
# - PRZECHOWUJE WARTOŚCI RÓŻNEGO TYPU (TYLKO W PYTHONIE)
# - WSZYSTKIE ELEMENTY SĄ INDEKSOWANE I MAJĄ ADRES W PAMIĘCI
# - ILOŚĆ ELEMENTÓW LISTY MOŻE ELEGAĆ ZMIANIE DYNAMICZNIE W PROGRAMIE
# - MOŻLIWOŚC MANIPULACJI ELEMENTAMI LISTY
# - NIESKOŃCZONA (ZALEŻNA OD PAMIĘCI), ILOŚĆ ELEMENTÓW NIE MUSI BYĆ PREDEFINIOWANA

# Interpretacja graficzna listy
# Zawartość: [0x][1][0x] <-> [0x][2][0x] <-> [0x][3][0x]
# Indeks:         0               1               2
# Adres:         0x100           0x104           0x108
# Klucz do:      0x104           0x108
# Klucz od:                      0x100           0x104

# DEKLARACJA LISTY
lista = [1, 2, "c", ]

print(lista)                      # WYPISANIE LISTY W CAŁOŚCI
print(lista[0])                   # WYPISANIE ELEMENTU LISTY POD INDEKSEM
lista[2] = 3                      # NADPISANIE ELEMENTU LISTY
lista += [4, 5]                   # ŁĄCZENIE LISTY
lista *= 2                        # MNOŻENIE LISTY
lista.append(6)                   # DOPISYWANIE ELEMENTU DO LISTY ZA POMOCĄ METODY
lista.append([7,8])               # DOPISYWANIE LISTY JAKO ELEMENTU DO LISTY ZA POMOCĄ METODY
lista.insert(2, 9) # DOPISYWANIE ELEMENTU DO LISTY POD PODANYCH INDEKSEM ZA POMOCĄ METODY
lista.remove(9)                   # USUWANIE ELEMENTU Z LISTY
dlugosc_listy = len(lista)        # SPRAWDZANIE DŁUGOŚCI LISTY ZA POMOCĄ FUNKCJI
ilosc_wystapien = lista.count(3)  # LICZENIE ILOŚCI WYSTĄPIEŃ ELEMENTU
gdzie_wystapil = lista.index(3)   # SPRAWDZANIE GDZIE PO RAZ PIERWSZY WYSTAPIL ELEMENT

print("Lista: ", lista)
print("Długość listy: ", dlugosc_listy)
print("Ilość wystąpień 3: ", ilosc_wystapien)
print("Indeks wystąpienia 3: ", gdzie_wystapil)
print("Element elementu: ", lista[11][0]) # ODWOŁANIE SIĘ DO ELEMENTU LISTY ZAGNIEŻDZONEJ

lista2 = [2, 1, 3, 5, 4]
print("Min: ", min(lista2))
print("Max: ", max(lista2))
lista2.sort()                     # SORTOWANIE LISTY
print("Sort: ", lista2)
lista2.reverse()                  # ODWRACANIE LISTY
print("Reverse: ", lista2)
lista2.clear()                    # CZYSZCZENIE LISTY DO PUSTA
print("Clear: ", lista2)


# NAPIS W PYTHONIE JEST TABLICĄ POJEDYŃCZYCH NAPISÓW
# (PYTHON NIE POSIADA TYPU DANYCH CHAR)
napis = "Hello"
# napis = "H" + "e" + "l" + "l" + "o"
# index:  [0]   [1]   [2]   [3]   [4]
print(napis[0])