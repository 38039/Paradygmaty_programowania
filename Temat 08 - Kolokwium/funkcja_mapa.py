# Napisz funkcję mapę, która otrzymuje jako parametry funkcję dwuargumentową, oraz dwie listy, a zwraca listę wyników
# wywołań otrzymanej funkcji dla kolejnych elementów otrzymanych int (pierwszy argument z pierwszej, drugi z drugiej
# np ( f.sumująca - [1,2,3,4][5,6,7] -> [6,8,10])

def mapa(f, lista1, lista2):
    return [f(a,b) for a,b in zip(lista1,lista2)]