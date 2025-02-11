# ZADANIE 1:  SUMA KROTEK
#
# Napisz program, która dla listy dwuelementowych krotek stworzy nową listę (z użyciem append)
# zawierającą sumy elementów tych krotek. Program ma wypisać stworzoną listę.
# Do sumowania proszę nie używać funkcji sum.
#
# W programie posumuj krotki listy:
# [(1,2),(3,4),(5,6),(7,8)] (ma 'wyjść' [3,7,11,15])

list_of_tuples = [(1,2),(3,4),(5,6),(7,8)]
summed_tuples  = []

for element in list_of_tuples:
    summed_tuples.append(element[0] + element[1])

print(summed_tuples)