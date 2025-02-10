# TEMAT   3:  KOLEKCJE
# ZADANIE 4:  CYFRY RZYMSKIE
#
# WYMAGANIA:
# Maksymalna liczba plików: 1
# Rodzaj pracy:  Praca indywidualna
#
# TREŚĆ:
# Napisz program, który zamieni napis zawierający liczbę rzymską na liczbę całkowitą wg algorytmu:
#
# W pętli, używając indeksu, weź dwie kolejne litery napisu (wycięciem - ang. slicing,
# czyli z użyciem [ : ]) i sprawdź: jeżeli 'wartość rzymska' pierwszej jest większa
# lub równa drugiej to dodaj ją do sumy a jak mniejsza to odejmij.  Zwiększ indeks o 1.
# Pętla powinna zatrzymać się na przedostatnim znaku, wartość odpowiadająca ostatniemu
# znakowi ma być dodana po pętli. Proszę przy odwoływaniu się do ostatniego znaku nie
# korzystać z długości napisu ani z indeksu używanego w pętli.
#
# Wypisz sumę, czyli wartość 'arabską'.
# Przydatny będzie słownik zamieniający 'cyfry rzymskie' na wartości 'arabskie'.

dictionary = {
    "I" : 1    ,
    "V" : 5    ,
    "X" : 10   ,
    "L" : 50   ,
    "C" : 100  ,
    "D" : 500  ,
    "M" : 1000
}
input  = input().upper()
output = 0

for num in range(len(input)-1):
    formated_input  = input[num:num+2]
    first_num       = dictionary.get(formated_input[0], 0)
    second_num      = dictionary.get(formated_input[1], 0)
    if first_num >= second_num: output+=first_num
    else:                       output-=first_num
output += dictionary.get(input[-1], 0)

print(output)