# ZADANIE 2:  LATA PRZYSTĘPNE
#
# Napisz program tworzący listę lat przestępnych z przedziału podanego z klawiatury (wczytujemy dwie wartości)
# - przy czym rok początkowy ma być uwzględniany w sprawdzaniu, a końcowy nie.
#
# Przypominam, że rok jest przestępny, jeżeli jest podzielny przez 4,
# ale nie jest podzielny przez 100, chyba że jest podzielny przez 400.
#
# Listę proszę stworzyć z użyciem list comprehension.
# Poprawność proszę sprawdzić podając przedział 1900-2001
# - rok 1900 nie ma się pojawić, a 2000 już tak

beginning_year = int(input())
ending_year    = int(input())

leap_years = [
    year for year in range(beginning_year, ending_year + 1)
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0
]

print(leap_years)