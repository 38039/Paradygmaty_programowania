# ** ZADANIE PRAKTYCZNE - GRA W ZGADNIJ LICZBĘ **

# OPIS ALGORYTMU:
# 1. Komputer losuje liczbę z przedziału 1 - 10
# 2. Komputer zaczyna inkrementację zmiennej (Co każdą próbę)
# 3. Gracz zostaje poproszony o zgadnięcie i wpisanie liczby
# 4. Program sprawdza, czy podana przez gracza odpowiedź jest poprawna
# 5. Gdy nie jest; program podaje podpowiedź (Wylosowana większa/mnniejsza)
# 6. Gdy     jest; program podaje ilość podejść i kończy działanie

# KOD PROGRAMU:
from random import randint                    # IMPORT FUNKCJI PSEUDOLOSUJĄCEJ

wylosowana = randint(1, 10)             # PSEUDOLOSOWANIE Z PRZEDZIAŁU 1-10 DO ZMIENNEJ
odpowiedz  = -1                               # ODPOWIEDŹ DOMYŚLNIE POZA PRZEDZIAŁEM LOSOWANIA
iterator   =  0                               # ZMIENNA PRZECHOWYWUJĄCA ILOŚĆ PRÓB

print("Podaj liczbę z przedziału 1 - 10")
while odpowiedz != wylosowana:                # PONIEWAŻ DOMYŚLNIE WARUNEK JEST SPEŁNIONY PĘTLA ZACZNIE SIĘ Z PROGRAMEM
    iterator += 1                             # INKREMENTUJ ZA KAŻDYM WYKONANIEM PODEJŚCIEM
    odpowiedz = int(input("Podaj liczbę: "))  # INPUT DO ZMIENNEJ WRAZ Z KONWERSJĄ TYPU DO INT

    if   odpowiedz > wylosowana : print("Wylosowana liczba jest mniejsza")
    elif odpowiedz < wylosowana : print("Wylosowana liczba jest większa")
    else                        : print(f"Ilość podejść: {iterator}")