# TEMAT   1:  INSTRUKCJE STERUJĄCE
# ZADANIE 4:  ZGADUJ ZGADULA
#
# WYMAGANIA:
# Maksymalna liczba plików: 1
# Rodzaj pracy:  Praca indywidualna
#
# TREŚĆ:
# Napisz program, który wylosuje liczbę całkowitą z zakresu 1-10 a następnie pozwoli na zgadnięcie
# tej liczby w 3 próbach. Program ma podawać po każdej nieudanej próbie, czy podana liczba jest większa
# czy mniejsza od wylosowanej. Po osiągnięciu zadanej liczby nieudanych prób program ma wypisać komunikat
# o porażce, a w wypadku zgadnięcia, komunikat o sukcesie. W programie należy wykorzystać konstrukcję while-else.
#
# Przykład losowania liczb w Pythonie (do przerobienia i wykorzystania):
# import random
# print(random.randint(1, 10))

import random

target = random.randint(1, 10)

turn = 0
while turn < 3:
    guess = int(input())

    if guess > target:
        print("Wieksza")
    elif guess < target:
        print("Mniejsza")
    else:
        print("Wygrales")
        break

    print()
    turn += 1
else:
    print("Przegrales")