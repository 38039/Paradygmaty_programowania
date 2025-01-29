# TEMAT   2:  INSTRUKCJE STERUJĄCE
# ZADANIE 2:  SZUKANIE 'A'
#
# WYMAGANIA:
# Maksymalna liczba plików: 1
# Rodzaj pracy:  Praca indywidualna
#
# TREŚĆ:
# Napisz program, który policzy (i wypisze) ile, w napisie wprowadzonym z klawiatury,
# znajduje się liter 'a' i 'A' (łącznie - wynikiem ma być jedna liczba).
# Użyj pętli for. W zadaniu może tylko raz wystąpić instrukcja if.
# NIE WOLNO używać range, lower ani count.

text = input()
count = 0

for x in text:
    if x=='a' or x=='A':
        count += 1

print(count)