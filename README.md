# PARADYGMATY PROGRAMOWANIA 2024 / 2025
**Labolatorium - Zbiór zadań i rozwiązań**

---

https://www.youtube.com/watch?v=KNyG5AwlKGE

### Paradygmaty programowania – co to jest?

**Paradygmat programowania** to styl lub sposób pisania programów, który określa, jak programista powinien podchodzić do organizacji kodu i rozwiązywania problemów. Każdy paradygmat definiuje zestaw zasad, wzorców oraz praktyk, które pomagają tworzyć czytelne, efektywne i logiczne programy. Paradygmaty oferują różne sposoby myślenia i podejścia do tworzenia aplikacji, co pozwala programistom wybrać najodpowiedniejsze narzędzia do konkretnego problemu.

### Popularne paradygmaty programowania

1. **Programowanie proceduralne**  
   - Paradygmat oparty na strukturalnym podejściu do pisania kodu. 
   - Program jest zorganizowany w funkcje i procedury, które wykonują konkretne zadania.
   - Operuje na danych przechowywanych w zmiennych oraz wykonuje instrukcje krok po kroku.
   - **Przykłady języków:** C, Pascal.

   **Cechy:**  
   - Podział kodu na funkcje.
   - Reużywalność kodu.
   - Jego wadą może być trudność w utrzymaniu kodu w dużych projektach.

---

2. **Programowanie obiektowe (OOP)**  
   - Paradygmat skupiony na obiektach, które reprezentują rzeczywiste byty lub abstrakcje.
   - Obiekty łączą dane (atrybuty) z kodem (metody) w jedną całość.
   - Używa koncepcji takich jak: klasy, dziedziczenie, polimorfizm, enkapsulacja.
   - **Przykłady języków:** Java, Python, C++, C#.

   **Cechy:**  
   - Łatwość modelowania rzeczywistego świata.
   - Zapewnienie lepszej organizacji i modularności.
   - Wysoka reużywalność kodu.

---

3. **Programowanie funkcyjne**  
   - Paradygmat oparty na funkcjach matematycznych i wyrażeniach bez zmieniania stanu programu (brak efektów ubocznych).
   - W funkcjonalnym podejściu unika się zmiennych i stanu globalnego.
   - Kod jest bardziej deklaratywny – mówi **co robić**, a nie **jak zrobić**.
   - **Przykłady języków:** Haskell, Lisp, Scala, częściowo Python.

   **Cechy:**  
   - Ułatwia programowanie współbieżne i obsługę dużej ilości danych.
   - Może prowadzić do trudności w zrozumieniu dla początkujących.

---

4. **Programowanie deklaratywne**  
   - Paradygmat, w którym opisuje się, **co ma zostać zrobione**, ale nie określa się, **jak to zrobić**.
   - Programista definiuje oczekiwany wynik, a szczegółowa implementacja pozostaje ukryta.
   - **Przykłady języków:** SQL (dla baz danych), HTML (dla struktury stron WWW).

   **Cechy:**  
   - Intuicyjne w pewnych zastosowaniach (np. zapytania do bazy danych).
   - Nie zawsze daje pełną kontrolę nad wykonywaniem programu.

---

5. **Programowanie logiczne**  
   - Paradygmat, który koncentruje się na regułach i faktach w logice, używanych do rozwiązywania problemów.
   - Logika definiuje zasady, a silnik (np. interpreter) sam rozwiązuje problem.
   - **Przykłady języków:** Prolog.

   **Cechy:**  
   - Skupienie na problemach logicznych i systemach eksperckich.
   - Mniej popularny w zastosowaniach komercyjnych.

---

6. **Programowanie reaktywne**  
   - Skupia się na przepływie danych oraz reagowaniu na zmiany stanu.
   - Stosowane m.in. w tworzeniu aplikacji w czasie rzeczywistym (np. aplikacje UI, systemy asynchroniczne).
   - **Przykłady:** RxJS, React.

---

### Dlaczego paradygmaty są ważne?

- **Pomagają rozwiązywać różne typy problemów:** Każdy z paradygmatów jest bardziej odpowiedni do określonych typów zadań.
- **Organizują kod:** Paradygmaty nadają strukturę tworzonemu oprogramowaniu, co ułatwia późniejszą jego aktualizację, rozszerzanie i utrzymanie.
- **Zwiększają produktywność:** Każdy z paradygmatów zawiera uniwersalne zasady i wzorce, które pozwalają unikać błędów i tworzyć wydajne rozwiązania.

Zrozumienie i zastosowanie różnych paradygmatów programowania jest kluczowe dla rozwoju jako programista! Dzięki różnorodności można podejść do problemów na kilka sposobów i wybrać rozwiązanie najlepiej dopasowane do danego przypadku.

# Spis zagadnień obejmujących dany temat:
## Programowanie niestrukturalne: ...
## Instrukcje sterujące:
- Operatory matematyczne
- Operatory porównania
- Instrukcje warunkowe
- Operatory logiczne
- Pętle
## Kolekcje:
- Lista
- Krotka
- Słownik

# Autorska Dokumentacja:
## Importy które już są w kodzie:
```py
from haskell import Haskell, lift1, lift2, flip
from operator import add, truediv, pow
from functools import reduce
```

```py
Fliped_truediv = flip(truediv)
s=suma(1,2) ---> s=(lambda a, b: a + b)(1,2)
def add(a,b) :
 return a+b
list(map(add, list1, list2)) # [6, 8, 10, 12]
---> list(map(lambda a, b: a+b, list1, list2)) #[6, 8, 10, 12]
```
If in doubt read this:
```
def jakaś_funkcja(x):
 return inna_funkcja(x)
można zastąpić zapisem:
jakaś_funkcja = inna_funkcja
(analogicznie w wypadku lambdy: jakaś_funkcja = lambda x: inna_funkcja(x)
to to samo co: jakaś_funkcja = inna_funkcja
```
## Schemat funkcji:
```
def jakas_funckja(*args, **kwargs):
 # cialo funkcji
 return 0
```
## Rekurencja z wyrażeniem warunkowym:
```py
def silnia(n):
#<wyr1> if <war> else <wyr2>
return 1 if n==0 else return n * silnia(n-1)
```

## Rekurencja ogonowa:
```py
def s(n, acc=1) :
if n>0 :
 acc = n*acc
 n = n-1
 return s(n, acc)
 return acc
```
## Składanie funkcji
Składanie funkcji pozwala na łączenie dwóch funkcji, gdzie wynik jednej funkcji staje się wejściem do
drugiej.
**Przykład:**
```py
def upper(napis):
 return napis.upper()
def strip(napis):
 return napis.strip()
compose = lambda f, g: lambda x: f(g(x))
duże = compose(upper, strip)
print(duże(" ala ma kota ")) # Wynik: "ALA MA KOTA"
```
## Składanie funkcji
```py
map_h = Haskell(map,2)
sum_h = Haskell(sum)
pow_h = flip(pow)
mul_h = flip(mul)
def haskell_vec_length(vec):
 return (pow_h(1/2) ** sum_h ** map_h(pow_h(2)))(vec)
```
Kolejnosc wykonywania funkcji: map_h(pow_h(2)) -> sum_h -> map_h(pow_h(1/2)) 
## Lambda: 
Anonimowe funkcje definiowane za pomocą słowa kluczowego lambda. Są przydatne dla
prostych operacji.
```py
dodaj = lambda x, y: x + y
print(dodaj(2, 3)) # Wynik: 5
Lambda argument1, argument2: działania_które_ma_wykonywać
```
## Fold: 
Agreguje elementy struktury danych w pojedynczą wartość.
```py
from functools import reduce
lst = [1, 2, 3, 4]
wynik = reduce(lambda acc, x: acc + x, lst, 0)
print(wynik) # Wynik: 10
```
## Flip
(zamienia miejscem Flip(funkcja(a,b)) -> funkcja(b,a)
**Przykład użycia funkcji flip:**
```py
list1 = [10, 20, 30, 40]
list2 = [1, 2, 3, 4]
def sub(a, b):
return a – b
flipped_sub = Flip(sub)
wynik = list(map(flipped_sub, list1, list2))
print(wynik)
# Wynik to będzie: [-9, -18, -27, -36]
```
## Przykład użycia funkcji map:
```py
list1=[1,2,3,4]
list2=[5,6,7,8]
def add(a, b) :
return a+b
wynik = list(map(add, list1, list2))
print(wynik)
#Wynik to będzie : [6, 8, 10, 12]
```
## Przykład Częściowa aplikacja:
```py
def flip(func):
 return lambda y, x: f(x, y)
dziel_przez_3 = partial(flip(truediv),3); # 3 staje się domyślnym argumentem funkcji truediv
print(dziel_przez_3(7))
# Wynik to będzie: 2.333
```
## Przykład funkcji filter():
```py
lista=[1,2,3,4,5,6,7,8]
def filt(a) :
if a>5 :
 return True
else :
 return False
list(filter(filt, lista))
# Wynik : [6,7,8]
```
## Curring
Rozbija funkcje która ma dwa argumenty na dwie funkcje które mają jeden argument
```py
def f(x, y):
 return x + y
def curry(func):
 return lambda x: lambda y: func(x, y)
curried_f = curry(f)
step1 = curried_f(3)
result = step1(4)
print(result) # Wynik: 7
```
## Mul (mnożenie)
Przykład użycia funkcji mul:
```py
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
def Mul(a, b):
return a * b
wynik = list(map(Mul, list1, list2))
print(wynik)
# Wynik to będzie: [5, 12, 21, 32]
```
## Lifting :
```py
def lift1(f, m_a): #f = funkcja którą chcemy zamienic zeby obslugiwała typ złożony
if m_a == None : return None
return f(m_a)
Zapobiega niepowodzeniu programu przez obsługe None
```