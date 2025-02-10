# Pierwsze wystąpienie liczby w liście zwraca jej indeks

def wystapienie(lista, liczba):
    return lista.index(liczba) if liczba in lista else -1