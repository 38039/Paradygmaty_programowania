# DEFINICJA FUNKCJI:
# def NAZWA_FUNKCJI(ARGUMENT, ARGUMENT, ...):
def suma(a,b):
    return a+b

# MOŻLIWOŚĆ PREDEFINIOWANIA ARGUMENTÓW:
def roznica(a,b=1):
    return a-b

# RETURN ZWRACA WYNIK JAKO WARTOŚĆ FUNKCJI

# WYWOŁANIE FUNKCJI:
print(suma(2,4))

x = roznica(2)
print(x)

# PRZECIĄŻENIE ZDEFINIOWANEGO ARGUMENTU:
print(roznica(2,4))