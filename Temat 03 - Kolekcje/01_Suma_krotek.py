# TEMAT   3:  KOLEKCJE
# ZADANIE 1:  SUMA KROTEK
#
# WYMAGANIA:
# Maksymalna liczba plików: 1
# Rodzaj pracy:  Praca indywidualna
#
# TREŚĆ:
# Napisz program w Pythonie rysujący "choinkę"
#
# Napisz program, która dla listy dwuelementowych krotek stworzy nową listę (z użyciem append)
# zawierającą sumy elementów tych krotek.
# Program ma wypisać stworzoną listę.
# Do sumowania proszę nie używać funkcji sum.
#
# W programie posumuj krotki listy:
# [(1,2),(3,4),(5,6),(7,8)] (ma 'wyjść' [3,7,11,15])

input = [(1,2),(3,4),(5,6),(7,8)]
output = []

for para in input:
    output.append(para[0] + para[1])

print(output)