lista = ["s", "k", "o", "w"]

# ITEROWANIE PO ELEMENTACH LISTY NA PODSTAWIE PĘTLI WHILE
i = 0
while i < len(lista):
    print(lista[i])
    i += 1

# ITEROWANIE PO ELEMENTACH LISTY NA PODSTAWIE PĘTLI FOR
# PĘTLA FOR - PĘTLA OBIEKTOWA - ITERUJE PO ELEMENTACH KOLEKCJI (W TYM PRZYPADKU LISTY)
# ZMIENNA TYMCZASOWA X JEST NADPISYWANA PRZEZ AKTUALNIE ITEROWANY ELEMENT KOLEKCJI
for x in lista:
    print(x)

# FUNKCJA RANGE() - TWORZY KOLEKCJE ELEMENTÓW Z DANEGO PRZEDZIAŁU
# DOMYŚLNA POSTAĆ FUNKCJI: range(...)
# range(OD_KTÓREGO_ELEMENTU, DO_KTÓREGO_ELEMENTU, SKOK_O_ILE)
# WYMAGANE RZUTOWANIE NA LISTĘ BY UZYSKAĆ CZYTELNĄ KOLEKCJĘ
print(list(range(10)))