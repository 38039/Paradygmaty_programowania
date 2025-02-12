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
## Funkcje
- Zbiory

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

# PARADYGMATY PROGRAMOWANIA 2024/25 - EGZAMIN

## 1. Czym jest Programowanie Logiczne?
Programowanie logiczne to paradygmat programowania, w którym program jest definiowany jako zbiór faktów i reguł, a wykonanie polega na zadawaniu zapytań i rozwiązywaniu ich na podstawie logiki formalnej. Główną ideą jest deklaratywne określenie co program ma zrobić, a nie jak ma to zrobić, co odróżnia je od tradycyjnego programowania imperatywnego.
## Cechy kluczowe:
- Opiera się na logice formalnej
- Używa reguł i faktów
- Silnik wnioskowania
- Brak jawnego sterowania przepływem programu

Najpopularniejszym językiem wykorzystującym podejście logiczne jest **Prolog**.
```
rodzic(jan, piotr).
rodzic(piotr, adam).

dziadek(X, Y) :- rodzic(X, Z), rodzic(Z, Y).

?- dziadek(jan, adam).
```

---

## 2. Czym są i jakie są różnice między Paradygmatami Imperatywnymi i Deklaratywnymi?
Paradygmaty imperatywne i deklaratywne to dwa główne sposoby podejścia do programowania. Różnią się one przede wszystkim tym, jak definiujemy i kontrolujemy przepływ programu.

## Paradygmat imperatywny
- Polega na opisywaniu kroków, jakie należy wykonać, aby osiągnąć określony rezultat.
- Programista określa jak program ma działać, definiując instrukcje sterujące przepływem wykonania
- Charakterystyczne dla języków programowania, takich jak; C, Java, Python

**Przykład imperatywny** (sumowanie liczb)
```py
numbers = [1, 2, 3, 4, 5]
sum = 0
for num in numbers:
    sum += num
```

## Paradygmat deklaratywny
- Skupia się na opisie rezultatu, a nie na szczegółowych krokach wykonania.
- Programista określa co ma być osiągnięte, a sposób wykonania jest pozostawiony językowi lub silnikowi wykonawczemu.
- Typowe dla języków takich jak; HTML, CSS, SQL, Prolog, Haskell

**Przykład deklaratywny** (sumowanie liczb za pomocą funkcji wbudowanej)
```py
numbers = [1, 2, 3, 4, 5]
sum = sum(numbers)
```

---

## 3. Czym jest funkcja ENUMERATE w Pythonie?
Polecenie enumerate(list) z listy elementów tworzy pary; (numer_elementu, element). Służy do numerowania elementów w iterowalnym obiekcie, takim jak lista, krotka czy ciąg znaków. Zwraca ona obiekt typu enumarate, który można przerzutować na listę krotek, gdzie każda krotka zawiera indeks i odpowiadający mu element.
```py
# SKŁADNIA
enumerate(iterable, start=0)

# iterable  - obiekt iterowalny (który chcemy ponumerować
# start     - początkowa wartość indeksu (opcjonalnie)
```
Przykład użycia enumarate
```py
fruits = ["jabłko", "banan", "wiśnia"]

# WYPISYWANIE ELEMENTÓW I INDEKSÓW LISTY NA PODSTAWIE PĘTLI FOR
for index, fruit in enumerate(fruits):
    print(index, fruit)

# TWORZENIE LISTY Z INDEKSAMI
lista_z_indeksami = list(enumerate(fruits))

# OUTPUT
# 0 jabłko
# 1 banan
# 2 wiśnia
```
---
## 4. Czym jest SŁOWNIK w Pythonie?
Słownik to kolekcja elementów dostępnych przez klucz. Tworzony jako zbiór par klucz:wartość, przy czym klucz musi być unikalny i niezmienialny. Jest przydatny gdy trzeba szybko wyszukać wartości na podstawie unikalnych kluczy.
```py
# SKŁADNIA
slownik = {} # Pusty słownik

# Słownik z danymi
slownik = {
    "imie": "Jan",
    "wiek": 25,
    "miasto": "Warszawa"
}
```
Przykład dostępu do słownika
```py
# ZA POMOCĄ INDEKSU
print(slownik["imie"])

# ZA POMOCĄ METODY
print(slownik.get("imie", "Brak danych"))
```
Operacje na słowniku
```py
# DODAWANIE NOWEGO KLUCZA / WARTOŚCI
slownik["nazwisko"] = "Kowalski"

# MODYFIKACJA ISTNIEJĄCEJ WARTOŚCI DANEGO KLUCZA
slownik["wiek"] = 26

# USUWANIE ELEMENTU
del slownik["miasto"]  # ZA POMOCĄ DYREKTYWY
slownik.pop("wiek")    # ZA POMOCĄ METODY

# POBIERANIE LISTY KLUCZY
klucze = slownik.keys()

# POBIERANIE LISTY WARTOŚCI
wartosci = slownik.values()

# POBIERANIE LISTY PAR (KLUCZ-WARTOŚĆ)
pary = slownik.items()
```
---
## 5. Czym są METODY STATYCZNE (I KLASOWE) w Pythonie?
W Pythonie istnieją trzy główne rodzaje metod w klasach:
1. **Metody instancyjne** – operują na konkretnej instancji klasy i mają dostęp do jej atrybutów (używają self).
2. **Metody klasowe** (@classmethod) – odpowiada mniej więcej metodie statycznej z C++. Operują na samej klasie, a nie na instancji, i mają dostęp do atrybutów klasy poprzez cls. 
3. **Metody statyczne** (@staticmethod) – Nie operują ani na instancji, ani na klasie. Są zwykłymi funkcjami umieszczonymi w klasie dla lepszej organizacji kodu. Stosowana jest jako odpowiednik przeciążonego konstruktora. Zamiast instancji klasy otrzymuje klasę jako pierwszy parametr.

Metody statyczne w Pythonie to metody definiowane w klasach, które nie operują na obiekcie ani na samej klasie. Nie mają dostępu do atrybutów instancji (self) ani do atrybutów klasy (cls). Są one przydatne do grupowania powiązanych funkcji w obrębie klasy, ale bez konieczności tworzenia obiektu.

## METODA STATYCZNA
Składnia metody statycznej
```py
class MathOperations:
    @staticmethod
    def add(a, b):
        return a + b
```
Przykład użycia metody statycznej
```py
# Wywołanie metody bez tworzenia instancji
print(MathOperations.add(3, 5))
```

## METODA KLASOWA
Przykład metody klasowej
```py
class Example:
    class_variable = "Hello"

    @classmethod
    def get_class_variable(cls):
        return cls.class_variable
```
Przykład użycia metody klasowej
```py
# Można wywołać metodę na klasie
print(Example.get_class_variable())

# i instancji
obj = Example()
print(obj.get_class_variable())
```
---

# 6. Czym jest REKURECJA OGONOWA i jak działa w Pythonie?
**Rekurencja ogonowa** to szczególny rodzaj rekurencji, w której wywołanie rekurencyjne jest ostatnią operacją wykonywaną w danej funkcji przed jej zakończeniem. Oznacza to, że nie trzeba przechowywać żadnych dodatkowych informacji na stosie wywołań, co teoretycznie pozwala kompilatorowi lub interpreterowi na optymalizację i zamianę rekurencji na pętlę.

Jednak **Python nie wspiera optymalizacji rekurencji ogonowej**, ponieważ stos wywołań w Pythonie ma ograniczoną głębokość i interpreter nie zamienia wywołań rekurencyjnych na iteracje. Dlatego w praktyce głęboka rekurencja w Pythonie może prowadzić do błędu RecursionError. Lepszym rozwiązaniem jest użycie głębokiej pętli.

## Zwykła rekurencja
```py
def silnia(n):
    if n == 0: return 1
    return n * silnia(n - 1)
```
Każda funkcja rekurencyjna musi czekać na wynik poprzedniej, co zwiększa głębokość stosu.

## Rekurencja ogonowa
```py
def silnia_ogonowa(n, wynik=1):
    if n == 0: return wynik
    return silnia_ogonowa(n - 1, n * wynik)
```
Zmienna wynik przechowuje / nadpisuje już aktualny wynik, więc nie trzeba przechowywać poprzednich stanów na stosie.

---

## 7. Czym jest CZĘŚCIOWA APLIKACJA i jej wynik będzie wynosić?

---

## 8. Programowanie funkcyjne/łączenie funkcji

---

## 9. Funkcje wyższego rzędu i 3 przykłady