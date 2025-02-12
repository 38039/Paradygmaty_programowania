# ZADANIE 3: SZUKANIE 'A' INDEKSY
#
# Napisz drugą wersję programu z ZADANIA 2, która zamiast zliczać litery 'A' i 'a' wypisze ich położenia (indeksy).
# Należy użyć pętli for BEZ range. Ponadto w programie nie może wystąpić żadne działanie arytmetyczne
# (dodawanie, odejmowanie ...) - podpowiedź: enumerate

text = input()

for i, elem in enumerate(text):
    if elem == 'a' or elem == 'A': print(i)