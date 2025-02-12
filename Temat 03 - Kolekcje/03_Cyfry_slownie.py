# ZADANIE 3:  CYFRY SŁOWNIE
#
# Napisz program, który zamieni napis zawierający ciąg cyfr
# (czyli liczbę ale zapisaną jako string) na napis 'słowny'
# (np. '1410' na 'jeden cztery jeden zero ').
# Znaki inne niż cyfry należy pomijać. Należy wykorzystać słownik zawierający liczebniki
# ('zero', 'jeden', itd). Odwołania do słownika proszę robić odwołania jak do tablicy
# (nawiasami [ ] ) a nie metodą get. Program na koniec ma wypisać stworzony napis (nie listę).
#
# Przydatne:
# "" lub '' - pusty napis (np. napis = "")
# in   - operator który zwraca wartość logiczną
# czy element znajduje się w liście,krotce, itd. (np. if element in lista)

numbers_dictionary = {
    '0' : 'zero '     ,
    '1' : 'jeden '    ,
    '2' : 'dwa '      ,
    '3' : 'trzy '     ,
    '4' : 'cztery '   ,
    '5' : 'pięć '     ,
    '6' : 'sześć '    ,
    '7' : 'siedem '   ,
    '8' : 'osiem '    ,
    '9' : 'dziewięć '
}

numbers_from_user       = input()
numbers_from_dictionary = ''

for number in numbers_from_user:
    if number in numbers_dictionary:
        numbers_from_dictionary += numbers_dictionary[number]

print(numbers_from_dictionary)