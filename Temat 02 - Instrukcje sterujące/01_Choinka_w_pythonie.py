# ZADANIE 1:  CHOINKA W PYTHONIE
#
# Napisz program w Pythonie rysujący "choinkę"
#
# Czyli funkcja ma mieć 3 parametry - dwie liczby całkowite
# Liczba poziomów powinna być pobierana z klawiatury.
# Choinka o parzystej liczbie poziomów powinna zostać "wyrysowana" gwiazdkami, a o nieparzystej - hashami (#).
# Po wyrysowaniu choinki program ma ponownie pobrać liczbę poziomów i wyrysować nową choinkę.
# Rysowanie choinek ma być powtarzane wielokrotnie (w pętli while) aż do wyrysowania choinki
# o wysokości 7 (choinka o tej wysokości też ma zostać wyrysowana).
# Rysowanie pojedynczej choinki powinno być zawarte w jednej pętli for
# (z użyciem range oraz 'mnożenia liczby przez napis').

h = 0
while h < 7:
    x = int(input("Podaj liczbe: "))
    h = x

    if x % 2 == 0 : tree = '*'
    else          : tree = '#'

    space = x
    paint = 1
    for i in range(x):
        space = space - 1
        print(space * " " + paint * tree)
        paint = paint + 2
    print()