# ZADANIE 4: POCHODNA
#
# Napisz funkcję derivative, która otrzyma jako argumenty FUNKCJĘ (f), punkt, w którym liczymy pochodną (x)
# i przyrost ( h), a zwróci przybliżoną wartość pochodnej funkcji f w punkcie x.
# Przybliżoną wartość pochodnej uzyskuje się ze wzoru na iloraz różnicowy:
# (f(x+h) - f(x)) / h
#
# Niech w funkcji derivative h będzie parametrem z wartością domyślną równą 0.0001
#
# W programie wypisz wartości funkcji derivative dla:
# sin(x) w punkcie 1
# sin(x) w punkcie 0
# x^2 w punkcie 1 z przyrostem 0.00001
#
# Funkcja sin jest dostępna w module math (należy zaimportować moduł przez:
# import math - wtedy funkcja sin będzie dostępna jako math.sin
# Funkcję kwadratową x^2 należy zaimplementować samemu - wystarczy napisać funkcję otrzymującą x a zwracającą x**2.

import math

def derivative(f, x, h=0.0001): return (f(x + h) - f(x)) / h
def square(x):                  return x**2

print(derivative(math.sin, 1))
print(derivative(math.sin, 0))
print(derivative(square, 1, 0.00001))