# print("hello world")


# PEP8 - standard pisania kodu
# https://analityk.edu.pl/jak-pisac-kod-w-python-aby-byl-czytelny-pep8/


# mojaZmiennaTypuString - camelCase
# moja_zmienna_typu_sting - snake_case <- pythonowa składnia

# def funkcja():
#     """Moja funkcja"""
#     pass

# for x in lista:
#     wgwg
#     wrgwrg

#     # wrhwrhwrh
#     whwrh
#     whilewhwrh

#     wrhwrh


# funkcja()

# range()

# a = 1 + 2
# print(a)


# Lintery: autopep8, pylint, black, ruff


### ZMIENNE

# imie = "Łukasz"
# liczba = 123
# znak = "A"

# print("przed zmianą:")
# print(imie)
# print(znak)
# print(liczba)

# print("po zmianie:")

# imie = "Józek"
# liczba = liczba + 100
# znak = "ABCED"

# print(imie)
# print(znak)
# print(liczba)

# print("po kolejnej zmianie:")
# imie = 1234
# znak = -999.123

# # rzutowanie (casting) typów - int na str
# liczba = str(liczba) + "abc"

# print(imie)
# print(znak)
# print(liczba)

# rzutowanie
# liczba_float = 1.0
# liczba_int = 1

# print(type(liczba_float))
# print(type(liczba_int))
# print(liczba_int)

# print("casting int na float")
# liczba_int = float(liczba_int)
# print(type(liczba_int))
# print(liczba_int)


# łącznie napisów
# imie = "Łukasz"
# liczba = 123
# znak = "A"
# liczba_float = 1234.56789

# print(imie, liczba, znak)
# print(imie + " " + str(liczba) + znak + str(liczba_float))

# # f-sting, Python v3.6+
# print(f"{imie}{liczba}{znak}{liczba_float}")
# print(f"({imie})(liczba)(znak)(liczba_float)")

# # format
# print("%s %s %s %s" % (imie, liczba, znak, liczba_float))
# print("{} {} {} {}".format(imie, liczba, znak, liczba_float))

# print("Tutaj jest imie: {}\nTutaj jest liczba: {}\n{} {}".format(liczba, imie, znak, liczba_float))

# print(f"Tutaj jest liczba: {liczba}\nTutaj jest imie: {imie}\n{znak} {liczba_float}")

# print(f"{liczba=}\n{imie=}\n{znak}\n{liczba_float:.2f}\n{liczba_float}")
# liczba_float_round = round(liczba_float, 2)
# print(f"{liczba_float=}\n{liczba_float_round=}")


### ZADANIE 1
# Zdefiniuj kilka zmiennych, w różnych typach.
# Wyświetl je korzystając z print() i f-string, każda zmienna w oddzielnej linii.

# nazwisko = "kowalski"
# wiek = 35
# ulubiona_litera = "Z"

# print(nazwisko)
# print(wiek)
# print(ulubiona_litera)

# print(f"{nazwisko=}\n{wiek=}\n{ulubiona_litera=}")


### POBIERANIE INFORMACJI OD UŻYTKOWNIKA

# info_od_usera = input("tekst zachęty: ")
# print(info_od_usera)
# print(type(info_od_usera))


#### ZADANIE 2

# Pobierz od użytkownika jego imię i nazwisko (osobne zapytania) i wyświetl napis "Cześc, {imie} {nazwisko}!"
