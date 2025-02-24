### 1.KOLEJNOŚĆ AKCJI PRZY WYWOŁANIU PODPROGRAMU:
  1. umieszczenie argumentów na stosie
  2. przechowanie stanu podprogramu wywołującego
  3. przekazanie sterowania do podprogramu
  4. alokacja zmiennych lokalnych
---
### 2.PRAWDZIWE:
  - Funkcja z rekurencją ogonową zazwyczaj wymaga dodatkowych parametrów
  - Jeżeli wartość zwracana przez funkcję z rekurencją ogonową jest wyliczana w wyrażeniu to nie może w nim wystąpić wynik kolejnego wywołania rekurencyjnego
  - Można tak zrealizować 'obsługę' rekurencji ogonowej, że nie istnieje ryzyko przepełnienia stosu w wyniku znaczącej liczby wywołań rekurencyjnych
---
### 3.WADY PROGRAMOWANIA FUNKCYJNEGO:
  - Trudność w realizacji operacji korzystających ze skutków ubocznych (np. operacje wejścia/wyjścia, generowanie liczb pseudolosowych)
  - Nieokreślona kolejność wykonywania obliczeń
  - Nieefektywność dużych struktur z dostępem swobodnym (np. tablic)
  - Występowanie struktur potencjalnie nieskończonych
---
### 5.ZGODNOŚĆ TYPÓW:
  - Mają taką samą strukturę
  - Posiadają metody/własności potrzebne w momencie wykonywania na nich operacji (np. jak w kaczym typowaniu)
  - Mają tę samą nazwę
---
### 6.STRUKTURY STERUJĄCE PROGRAMOWANIA STRUKTURALNEGO:
  - Pętla
  - Sekwencja instrukcji
  - Instrukcja wyboru
---
### 7.MECHANIZMY PROGRAMOWANIA OBIEKTOWEGO:
  - Dziedziczenie
  - Enkapsulacja
  - Polimorfizm
---
### 10.WYRAŻENIA LAMBDA:
  - Może być zwrócone przez funkcję wyższego rzędu
  - Może być parametrem funkcji wyższego rzędu
---
### 11.PRAWDZIWE:
  - Czas życia zmiennej lokalnej zależy od pamięci, w której została utworzona
  - Zmienne mogą stać się nieosiągalne, mimo że ich czas życia jeszcze nie upłynął
  - Czas życia zmiennej globalnej jest równy czasowi działania programu
---
### 12.PĘTLE W PROGRAMOWANIU FUNKCYJNYM:
  - Mogą być zastąpione przez funkcje rekurencyjne
  - Mogą być zastąpione przez funkcje wyższego rzędu
---
### 13.PRAWDZIWE:
  - Zmiana stanu maszyny jest charakterystyczna dla paradygmatów imperatywnych
  - Paradygmaty deklaratywne nie precyzują jak ma zostać osiągnięte rozwiązanie problemu
---
### 15.OKREŚLANIE TYPU ZMIENNEJ:
  - Wywnioskowany z kontekstu
  - Nadany na podstawie przypisywanej wartości
---
### 16.PROTOKÓŁ PODPROGRAMU:
  - To sygnatura uzupełniona typem wartości zwracanej przez podprogram
  - Określa typ wyniku oraz liczbę, kolejność i ewentualnie typ parametrów
---
### 19.PRAWDZIWE:
  - Współprogram to podprogram, którego wykonanie może być wstrzymane i następnie wznowione w punkcie wstrzymania
---
20.ATRYBUTY ZMIENNYCH:
  - Czas życia
  - Adres
  - Nazwa
  - Zakres widoczności
---
### WYJAŚNIJ POJĘCIA:
**PROGRAMOWANIE LOGICZNE**
```
polega na definiowaniu relacji pomiędzy danymi oraz formułowaniu warunków logicznych, które powinny zostać spełnione. Nie opisuje się kolejności wykonywania instrukcji – programista podaje tylko reguły i fakty.
```
**TRWAŁE STRUKTURY DANYCH**
```
struktury, które nie są modyfikowane po utworzeniu – każda zmiana tworzy nową wersję zamiast nadpisywać istniejącą.
```
**LENIWA EWALUCJA** 
```
polega na opóźnionym obliczaniu wartości wyrażeń (dopiero wtedy, gdy są faktycznie potrzebne).
```
**FUNKCJE WYŻSZEGO RZĘDU**
```
funkcje, które mogą przyjmować jako argumenty inne funkcje lub zwracać funkcje jako wynik.
```
**CZĘŚCIOWA APLIKACJA**
```
technika polegająca na przekazaniu tylko części argumentów do funkcji, co powoduje zwrócenie nowej funkcji z "zablokowanymi" już argumentami.
```
**PRZEŹROCZYSTOŚĆ REFERENCYJNA** 
```
właściwość wyrażeń w programowaniu, oznaczająca, że wyrażenie zawsze zwraca tę samą wartość dla tych samych argumentów, niezależnie od kontekstu, w którym jest używane.
```
---
### WYJAŚNIJ POJĘCIA (PYTHON):
**MAP()**
```
stosuje podaną funkcję do każdego elementu z iterowalnego obiektu i zwraca nową kolekcję z przekształconymi wartościami.
```
**FILTER()**
```
stosuje podaną funkcję do każdego elementu kolekcji i zwraca tylko te elementy, dla których funkcja zwróciła True.
```
**REDUCE()**
```
stosuje podaną funkcję kumulatywnie do elementów kolekcji, redukując ją do jednej wartości.
```
