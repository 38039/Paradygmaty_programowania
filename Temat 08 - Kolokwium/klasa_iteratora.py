# Napisz klasę iteratora Kwadraty, której konstruktor dostaje 1 lub 2 argumenty.
# 2 argumenty określają początek i koniec przedziału, z którego brane są liczby.
# Podanie jednego argumentu oznacza podanie końca przedziału, a wartość początku wynosi wówczas...
# Iterator ma generować kwadraty kolejnych wartości całkowitch z podanego przedziału (2 -> 4, 8, 16)

class Kwadraty:
    def __init__(self, start, koniec=None):
        if koniec is None:
            self.start = 1
            self.koniec = start
        else:
            self.start = start
            self.koniec = koniec

        self.current = self.start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.koniec:
            raise StopIteration

        result = self.current ** 2
        self.current += 1
        return result