# ZADANIE 1: WSPÓLNE ELEMENTY
#
# Napisz funkcję znajdującą wspólne elementy dwóch sekwencji (list, krotek lub napisów).
# Znalezione wspólne elementy mają być zwracane jako lista
# (każdy element w tej liście ma wystąpić tylko raz! - wykorzystaj konwersję do zbioru).
#
# Przykładowo dla krotek:
# (3,3,4,5)
# (3,3,2,5)
#
# funkcja ma zwrócić:
# [3,5] albo [5,3]

tuple1 = (3, 3, 4, 5)
tuple2 = (3, 3, 2, 5)

def common_elements(seq1, seq2):
    return list(set(seq1) & set(seq2))

print(common_elements(tuple1, tuple2))