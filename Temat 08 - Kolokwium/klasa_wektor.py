# Klasa Wektor, która otrzyma listę jako argument.
# Doda do tej klasy metodę, aby można było dany Wektor wypisać przy pomocy print.
# Dodać metodę sumowania dwóch wektorów.

class Wektor:
    def __init__(self, lista):
        self.lista = lista

    def __repr__(self):
        return f"Wektor({self.lista})"

    def _add_(self, other):
        if len(self.lista) != len(other.lista):
            print("Wektory muszą mieć tę samą długość")
        return Wektor([x+y for x,y in zip(self.lista, other.lista)])