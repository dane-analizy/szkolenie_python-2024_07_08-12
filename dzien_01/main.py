# czyszczenie terminala, odpowiednik Ctrl-L
print("\033c", end="")


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

# PRZYWITANIE = "cześć"
# nazwisko_usera = input("Podaj swoje nazwisko: ")
# imie_usera = input("Podaj swoje imie: ")

# print(PRZYWITANIE, imie_usera, nazwisko_usera)

# PRZYWITANIE = "cześć"
# imie_usera = input("Podaj swoje imie: ")

# uzywamy już pobranego imienia w prompcie
# nazwisko_usera = input(f"Jak się nazywasz, {imie_usera}? ")

# f-string mozna wykorzystac do zbudowania nowej zmiennej typu str
# wynik = f"{PRZYWITANIE} {imie_usera} {nazwisko_usera}"
# print(wynik)


# operacje na stringach:

# s = "  aBcDe  FgH"
# print(s)

# s_wielkimi = s.upper()
# print(s_wielkimi)

# s_malymi = s.lower()
# print(s_malymi)

# s_jak_tytul = s.title()
# print(s_jak_tytul)

# s_bez_pustych_znakow = s.strip()
# print(s_bez_pustych_znakow)

# s_bez_spacji = s.replace(" ", "")
# print(s_bez_spacji)


## Sprawdzamy czy imie zostało wpisane wielką literą

# imie = input("Podaj imię: ")
# imie_wielka_litera = imie.title()
# print(f"{imie=}\n{imie_wielka_litera=}")

# if imie == imie_wielka_litera:
#     print("zgadza się")
# else:
#     print("nie zgadza się")


### ZADANIE

# Pobierz od użytkownika liczbę i sprawdź czy jest większa niż 100.
# Wypisz odpowiedni komunikat w zaleznosci od wartości wpisanej liczby.


## rozwiązanie 1

# liczba = input("Podaj prosze dowolna liczbe:")
# liczba = float(liczba)

# if liczba > 100:
#     print("Podana liczba jest wieksza niz 100")
# elif liczba == 100:
#     print("Podana liczba jest rowna 100")
# elif liczba < 50:
#     print("Podana liczba jest mniejsza niz 50")
# else:
#     print("Podana liczba jest mniejsza niz 100 i większa niż 50")


## rozwiązanie 2


# liczba = input("Podaje liczbę: ")

# if not liczba.isdigit():
#     print("to nie jest liczba")
#     exit() # kończymy program

# # jest liczbą - więc sprawdzamy warunki
# if int(liczba) > 100:
#     print("Liczba jest WIEKSZA niż 100")
# elif int(liczba) < 100:
#     print("Liczba jest MNIEJSZA niż 100")
# elif int(liczba) == 100:
#     print("Liczba jest równa 100")

# kwadrat liczby:
# x*x
# x**2
# pow(x, 2)

# szescian liczby:
# x*x*x
# x**3
# pow(x, 3)

#### ZADANIE

# Napisz program, który pobierze od użytkownika masę i wzrost,
# a następnie policzy BMI i wypisze wynik na konsolę.

# bmi = weight (kg) / height(m) **2


# rozwiazanie zadania

# wzrost = input("Czesc, podaj mi swoj wzrost w [cm]")
# masa = input("a teraz podaj mi swoja mase ciala w [kg]")

# wzrost = float(wzrost)
# masa = float(masa)

# bmi = masa / (wzrost / 100) ** 2
# print(f"Twoje BMI, przy wzroscie {wzrost} cm i wadze {masa} kg wynosi: {bmi:.1f}")


# rzutowanie na float w bezpieczny sposób

# def to_float(s):
#     try:
#         f = float(s)
#     except:
#         f = None
#     return f


# s = "12efwgf23.123"

# print(to_float(s))

# print(float(s))

# print("a to jest po wszystkim")

# rozwiazanie drugie


# masa = input("Podaj masę ciała w kg: ")
# if not masa.isdigit():
#     print("To nie jest liczba")
#     exit()

# wzrost = input("Podaj wzrost w cm: ")
# if not wzrost.isdigit():
#     print("To nie jest liczba")
#     exit()

# bmi = round(float(masa) / pow(float(wzrost/100), 2), 2)

# print("BMI: ", bmi)


### PĘTLE

zmienna = "ala ma kota"

# print(zmienna)
# print(zmienna)
# print(zmienna)
# print(zmienna)
# print(zmienna)

# print(zmienna, zmienna, zmienna, zmienna, zmienna)

# 5 przebiegów pętli
# for licznik in range(5):
#     print(licznik)
#     print(zmienna)


# print("range z samym stop:")
# for licznik in range(3):
#     print(licznik)

# print("range z start i  stop:")
# for licznik in range(10, 13):
#     print(licznik)

# print("range z start, stop i step:")
# for licznik in range(10, 20, 3):
#     print(licznik)


### ZADANIE

# Wypisz kolejne 10 potęg liczby 2, począwszy od potęgi 1 (czyli: 2^1, 2^2, ..., 2^10)

# for potega in range(1, 11):
#     potega_wynik = 2**potega
#     print(f"2^{potega} = {potega_wynik}")


### ZADANIE

# Wypisz tabliczkę mnożenia do 5x5 w kolejnych liniach, czyli:
# 1x1 = ..
# 1x2 = ..
# 1x5 = ..
# 2x1 = ..
# ..
# 5x5 = 25


# rozwiązanie 1
# for licznik_1 in range(1, 6):
#     for licznik_2 in range(1, 6):
#         wynik = licznik_1 * licznik_2
#         print(f"{licznik_1} x {licznik_2} = {wynik}")


# rozwiązanie 1 bardziej fancy

# for licznik_1 in range(1, 6):
#     for licznik_2 in range(1, 6):
#         wynik = licznik_1 * licznik_2
#         print(f"{licznik_1} x {licznik_2} = {wynik} \t", end="")
#     print()


# to nie jest rozwiązanie - poszukaj przyczyny
# for pierwsza_petla in range(2, 3):
#     for druga_petla in range(1, 11, 1):
#         wynik = pierwsza_petla**druga_petla
#         print(f"{pierwsza_petla} x {druga_petla} = {wynik} \t", end="")
#     print()


# zmienna = "ala ma kota"
# for _ in range(5):
#     print(zmienna)


# string jest listą
# lista = [4, 6246, 134, 1135, "262", 8579, "46", 234]
# lista = "napis"
# for element in lista:
#     print(element, type(element))


### ZADANIE

# Wydrukuj liczby od 1 do 100 razem z informacją czy liczba jest parzysta czy nieparzysta.

# i = 21
# print(i % 2)
# print(i // 2)

# rozwiązanie
# for i in range(1, 101):
#     if (i % 2) == 0:
#         print(f"{i} parzysta")
#     else:
#         print(f"{i} nieparzysta")


# rozwiązanie nieco bardziej "pythonoic"
# for i in range(1, 101):
#     if (i % 2):
#         print(f"{i} nieparzysta")
#     else:
#         print(f"{i} parzysta")


# break = przestan wykonywac petle
# continue = przestan wykonywac biezaca iteracje i idz do nastepnej

# jesli nieparzysta = nie wyswiatlaj nic
# for i in range(1, 101):
#     if i % 2:
#         continue

#     # if i > 50:
#     #     break

#     print(f"{i} parzysta")

# else:
#     print("else dla for się wykonał - pętla przeszła w całości")

# print("Koniec petli")


# pętla WHILE

# while warunek:
#     jakieś operacje

# while True:
#     print("działam")


# while False:
#     print("działam")

# też działają:
# break = przestan wykonywac petle
# continue = przestan wykonywac biezaca iteracje i idz do nastepnej


### ZADANIE

# Napisz pętlę while która będzie wyświetlała kolejne potęgi liczby 2 aż wartość potęgi (wynik potęgowania)
# nie przekroczy wartości podanej przez użytkownika.

# limit = int(input("Jaki jest limit? "))

# potega = 0
# wynik_potegowania = 2**potega

# while wynik_potegowania <= limit:
#     print(f"2 do potęgi {potega} = {wynik_potegowania}")
#     potega = potega + 1
#     # potega += 1
#     wynik_potegowania = 2**potega


# limit = int(input("Jaki jest limit? "))

# potega = 0

# while True:
#     wynik_potegowania = 2**potega
#     if wynik_potegowania > limit:
#         break
#     print(f"2 do potęgi {potega} = {wynik_potegowania}")
#     potega = potega + 1


# Czytanie plików
# nazwa_pliku = "test.txt"
# for linia in open(nazwa_pliku, encoding="utf-8"):
#     linia_czysta = linia.strip()
#     print(f"{len(linia_czysta)}: |{linia_czysta}|")


### ZADANIE

# Wczytaj tekst "Pana Tadeusza" i policz ile jest w nim NIEPUSTYCH linii.

# rozwiązanie
# nazwa_pliku = "pan-tadeusz.txt"

# liczba_wszystkich = 0
# liczba_niepustych = 0

# for linia in open(nazwa_pliku, encoding="utf-8"):
#     if len(linia.strip()):
#         liczba_niepustych += 1
#     liczba_wszystkich += 1

# print(f"{liczba_wszystkich=}\n{liczba_niepustych=}")


# enumerate() - licznik przejśc przez petle
# lista = "abcdefghij"
# for i, literka in enumerate(lista, start=1):
#     print(i, literka)


# rozwiązanie z enumerate()

# nazwa_pliku = "pan-tadeusz.txt"

# liczba_niepustych = 0

# for licznik, linia in enumerate(open(nazwa_pliku, encoding="utf-8"), start=1):
#     if len(linia.strip()):
#         liczba_niepustych += 1

# print(f"{licznik=}\n{liczba_niepustych=}")


# lista = "abcdefghij"
# print(lista[5])


### ZADANIE

# Wypisz wszystkie NIEPUSTE linie z pliku main.py, które nie są komentarzem.


# linie - utrudnienia:

# utrudnienie - komentarz nie od początku linii
print("ala ma kota")  # to jest komentarz na końcu linii


# rozwiązanie
nazwa_pliku = "main.py"

for numer_linii, linia in enumerate(open(nazwa_pliku, encoding="utf-8"), start=1):
    # if len(linia.strip()) and not linia.startswith("#"): # - przepuści linię z komentarzem i spacjami na początku
    # if len(linia.strip()) and "#" not in linia: # - to przepiści komentarze na końcu linii
    if len(linia.strip()) and not linia.strip().startswith("#"):
        print(numer_linii, linia, end="")
