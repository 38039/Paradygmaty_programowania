# TEMAT   3:  KOLEKCJE
# ZADANIE 5:  SPIS KONTATKÓW
#
# WYMAGANIA:
# Maksymalna liczba plików: 1
# Rodzaj pracy:  Praca indywidualna
#
# TREŚĆ:
# Dany jest "spis kontaktów" w postaci słownika:
# kontakty = {('Jan', 'Kowalski'):"123456789", ('Adam', 'Nowak'):"987654321" , ('Adam', 'Kowalski'): "600300900"}
# Wypisz numer telefonu Adama Nowaka (jednym printem - używając słownika).
# Napisz kod, który wypisze (używając pętli, przechodzącej po całym słowniku)  numery telefonu obu Kowalskich.

dictionary = {
    ('Jan'  , 'Kowalski') : "123456789" ,
    ('Adam' , 'Kowalski') : "600300900" ,
    ('Adam' , 'Nowak'   ) : "987654321"
}

print(dictionary[('Adam', 'Nowak')])

for (name, surname), num in dictionary.items():
    if surname == 'Kowalski':
        print(f"{surname} {num}")