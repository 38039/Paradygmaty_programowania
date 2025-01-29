# TEMAT   1:  INSTRUKCJE STERUJĄCE
# ZADANIE 3:  SZUKANIE 'A' INDEKSY
#
# WYMAGANIA:
# Maksymalna liczba plików: 1
# Rodzaj pracy:  Praca indywidualna
#
# TREŚĆ:
# Napisz program w Pythonie rysujący "choinkę"
#
# Napisz drugą wersję programu z zadania 2, która zamiast zliczać litery 'A' i 'a' wypisze ich położenia (indeksy).
# Należy użyć pętli for BEZ range. Ponadto w programie nie może wystąpić żadne działanie arytmetyczne
# (dodawanie, odejmowanie ...) - podpowiedź: enumerate

text = input()

for i, x in enumerate(text):
    if x=='a' or x=='A': print(i)