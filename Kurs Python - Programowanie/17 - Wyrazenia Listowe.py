lista = list(range(10))
print("Oryginalna Lista:", lista)

# NOWA_LISTA = [OPERACJA DEKLARACJA_PĘTLI]
nowa_lista = [i * 2 for i in lista]
print("Nowa Lista 1:", nowa_lista)

# NOWA_LISTA = [OPERACJA DEKLARACJA_PĘTLI WARUNEK]
nowa_lista2 = [i + 2 for i in lista if i % 2 == 0]
print("Nowa Lista 2:", nowa_lista2)