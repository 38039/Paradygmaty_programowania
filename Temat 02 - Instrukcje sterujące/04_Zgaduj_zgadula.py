# ZADANIE 4:  ZGADUJ ZGADULA
#
# Napisz program, który wylosuje liczbę całkowitą z zakresu 1-10 a następnie pozwoli na zgadnięcie
# tej liczby w 3 próbach. Program ma podawać po każdej nieudanej próbie, czy podana liczba jest większa
# czy mniejsza od wylosowanej. Po osiągnięciu zadanej liczby nieudanych prób program ma wypisać komunikat
# o porażce, a w wypadku zgadnięcia, komunikat o sukcesie. W programie należy wykorzystać konstrukcję while-else.
#
# Przykład losowania liczb w Pythonie (do przerobienia i wykorzystania):
# import random
# print(random.randint(1, 10))

from random import randint

drawn_number = randint(1, 10)

i = 0
while i < 3:
    i += 1
    guess = int(input())

    if   guess < drawn_number: print("Higher")
    elif guess > drawn_number: print("Lower")
    else:
        print("Correct")
        break

else: print("GAME OVER")