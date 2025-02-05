# Suma krotek za pomocą funkcji

def suma_krotek(lista):
    suma = []
    for krotka in lista:
        suma = krotka[0] + krotka[1]
        suma_krotek.append(suma)
    return suma_krotek