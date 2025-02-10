# Suma krotek i konkatynacja

def suma_krotek(lista):
    suma = []
    for krotka in lista:
        if isinstance(krotka[0], int):
            licznik = 0
            for num in krotka:
                licznik += num
            suma.append(licznik)
        else:
            suma.append(''.join(krotka))
    return suma