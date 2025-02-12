# ZADANIE 3: POLA FIGUR
#
# Napisz funkcję, która będzie otrzymywać jako argumenty krotki zawierające nazwę figury oraz dane potrzebne do obliczenia
# pola tej figury (np. koło - promień, prostokąt - długości boków). Funkcja może otrzymać na raz kilka figur do policzenia.
# Pola mają być  umieszczane w słowniku w którym kluczami są nazwy figur a wartościami listy ich pól.
# Funkcja ma zwracać stworzony słownik.
#
# Funkcja ma umieć policzyć pole dla figur:
# koło, kwadrat, prostokąt, trójkąt
#
# W main należy wywołać funkcję z danymi:
# koła o promieniach 3 i 4, kwadraty o bokach 2 i 3, prostokąt o bokach 1 i 2, trójkąt o wysokości 4 i podstawie 3
# i wypisać otrzymany słownik

import math

def count(*figure):
    glossary = {
        'koło': [],
        'kwadrat': [],
        'prostokąt': [],
        'trójkąt': []}

    for shape in figure:
        name = shape[0].lower()

        if name == "koło":
            factorOne = shape[1]
            result = math.pi * factorOne ** 2
            glossary["koło"].append(result)
        elif name == "kwadrat":
            factorOne = shape[1]
            result = factorOne ** 2
            glossary["kwadrat"].append(result)
        elif name == "prostokąt":
            factorOne = shape[1]
            factorTwo = shape[2]
            result = factorOne * factorTwo
            glossary["prostokąt"].append(result)
        elif name == "trójkąt":
            factorOne = shape[1]
            factorTwo = shape[2]
            result = factorOne * factorTwo * 0.5
            glossary["trójkąt"].append(result)

    return glossary


aspect = [
    ('koło ', 3),
    ('koło', 4),
    ('kwadrat', 2),
    ('kwadrat', 3),
    ('prostokąt', 1, 2),
    ('trójkąt', 3, 4)
]

outcome = count(*aspect)
print(outcome)