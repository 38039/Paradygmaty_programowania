# ZADANIE 6:  LICZBY PIERWSZE (DODATKOWE)
#
# Napisz program znajdujący (i wypisujący) wszystkie liczby pierwsze z zakresu 1-100.
# Wykorzystaj dwie pętle for z czego jedna ma być typu for-else

for number in range(1, 101):
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0: break
    else: print(number)