# czyszczenie terminala, odpowiednik Ctrl-L
print("\033c", end="")

### ===========


# Wyjątki

### ZADANIE

# Wyświetl wynik dzielenia jedynki przez kolejne liczby z zakresu od -10 do 10.


# rozwiązanie - zwróci błąd przy dzieleniu przez 0 i program przerwie swoje działanie

# for i in range(-10, 10):
#     wynik = 1 / i
#     print(wynik)


# obsługa błędów - kontrukcja try - except

# for i in range(-10, 10):
#     try:
#         wynik = 1 / i
#     except Exception as e: # każdy rodzaj błędu
#         print(f"nie mogę dzielić przez {i}, błąd {e}")
#     print(wynik)


# różne typy wyjątków:
# for i in [-2, -1, 0, "a", 1, 2]:
#     try:
#         wynik = 1 / i
#     except Exception as e: # każdy rodzaj błędu
#         print(f"nie mogę dzielić przez {i}, błąd {e}")
#     print(wynik)

# print(1/0)
# print(1/"a")

# for i in [-2, -1, 0, "a", (1, 2, "4"), 1, 2, {"k": 120, "v": 30}]:
#     try:
#         wynik = 1 / i
#     except ZeroDivisionError as e:
#         print(f"nie mogę dzielić przez zero, błąd {e}")
#         # wiecej czynnosci
#     except TypeError as e:
#         print(f"nie mogę dzielić przez ten typ danych ({i}), błąd {e}")
#     except Exception:
#         print("inny błąd dzielenia, błąd {e}")
#     print(wynik)

# import math

# for i in [-2, -1, 0, "a", 1, 2]:
#     try:
#         wynik = 1 / i
#         logarytm = math.log10(i)
#     except ZeroDivisionError as e:  # dzielenie przez zero
#         print(f"Dzielenie przez zero, {i}: {e}")
#     except ValueError as e:  # dzielenie przez błędną wartość
#         print(f"Błędna wartość, {i}: {e}")
#     except Exception as e:  # każdy inny rodzaj błędu
#         print(f"{i}, błąd {e}, {type(e)}")
#     print(wynik)


### ZADANIE

# Wczytaj dane z pliku bmi.csv (uwaga - w pliku jest błąd - jedna z liczb ma dodany znak)
# i policz oraz wypisz na konsoli wskaźnik BMI dla każdej kolejnej osoby.
# Obsłuż potencjalne błędy.


# otwieramy plik, ładujemy dane z linii, odpowiedni casting zmiennych i wyliczenie BMI

# nazwa_pliku = "bmi.csv"
# enc = "utf-8"
# separator = ";"

# lista = [linia.strip().split(separator) for linia in open(nazwa_pliku, encoding=enc)]

# for nr, elem in enumerate(lista, start=1):
#     imie = elem[0]
#     nazwisko = elem[1]
#     try:
#         wzrost_m = float(elem[2]) / 100
#         waga_kg = float(elem[3])
#     except ValueError:
#         print(f"Błędne dane o wzroście lub wadze dla {imie} {nazwisko} - linia {nr}")
#         continue

#     bmi = waga_kg / wzrost_m**2
#     print(f"BMI dla {imie} {nazwisko} wynosi {bmi:.2f}")


# lepiej rozdzieli try-except na kroki
# try:
#     wczytaj dane
# except
#     nie udało się wczytac danych

# try:
#     przelicz agregat
# except
#     nie udało się przeliczyć agregatów

# try:
#     scal agregaty
# except
#     nie udało się scalic danych

# try:
#     zapisz dane
# except
#     nie udało się zaspisac raporty


# Funkcje

# DRY - Don't Repeat Yourself

# użycie funkcji z parametrami
# bmi = wylicz_bmi(wzrost, waga)
# wylicz_bmi(wzrost, waga) # to nie zwraca wartości

# def wylicz_bmi(wzrost, waga):
#     bmi = waga / wzrost**2
#     # print(f"bmi w ciele funkcji: {bmi}")

#     return bmi


# print(wylicz_bmi(1.85, 60))
# print(wylicz_bmi(1.95, 89))


# przykład z użyciem funkcji:
# def wylicz_bmi(wzrost: float, waga: float) -> float:
#     """Funkcja wylicza wskaźnik BMI z podanych parametrów.

#     Parametry:
#         - wzrost - liczba typu float, wzrost w metrach
#         - waga - liczba typu float, waga w kilogramach

#     Wynik:
#         - wyliczony wskaźnik BMI
#     """
#     bmi = waga / wzrost**2
#     # print(f"bmi w ciele funkcji: {bmi}")
#     return bmi


# nazwa_pliku = "bmi.csv"
# enc = "utf-8"
# separator = ";"

# lista = [linia.strip().split(separator) for linia in open(nazwa_pliku, encoding=enc)]

# for nr, elem in enumerate(lista, start=1):
#     imie = elem[0]
#     nazwisko = elem[1]
#     try:
#         wzrost_m = float(elem[2]) / 100
#         waga_kg = float(elem[3])
#     except ValueError:
#         print(f"Błędne dane o wzroście lub wadze dla {imie} {nazwisko} - linia {nr}")
#         continue

#     bmi = wylicz_bmi(wzrost_m, waga_kg)
#     print(f"BMI dla {imie} {nazwisko} wynosi {bmi:.2f}")


### ZADANIE

# Przygotuj funkcję, która wyliczy na podstawie wagi i wzrostu (parametry) BMI.
# W przypadku pojawienia się wyjątku - wypisze na konsoli błąd i zwróci wartość -1.


# czyli popraw funkcję:

# def wylicz_bmi(wzrost_m, waga_kg):
#     bmi = waga_kg / wzrost_m**2
#     return bmi


# def czy_parzysta(liczba):
#     return bool(liczba % 2 == 0)

# print(czy_parzysta(1))
# print(czy_parzysta(2))


# rozwiazanie zadania:
# def wylicz_bmi(wzrost, waga):
#     try:
#         bmi = waga / wzrost**2
#         return bmi
#     except:
#         print("Błędne dane o wzroście lub wadze")
#         return -1


# to samo, nieco inaczej:

# def wylicz_bmi(wzrost, waga):
#     try:
#         bmi = waga / wzrost**2
#     except Exception as e:
#         bmi = -1
#         print("Błędne dane o wzroście lub wadze")
#     return bmi


# uzycie funkcji z rozwiazania
# bmi = wylicz_bmi("a", 78)
# if bmi < 0:
#     print("jakiś problem")
# else:
#     print(f"{bmi=}")


# funkcje moga wywoływać inne funkcje

# def daj_czyste_dane_z_pliku(nazwa_pliku):
#     plik = otworz_plik(nazwa_pliku)
#     dane = wczytaj_z_pliku(plik)
#     dane_czyste = oczysc_dane(dane)
#     return dane_czyste

# dane = daj_czyste_dane_z_pliku("bmi.csv")

### ZADANIE

# Napisz jedną lub zestaw funkcji pobierającą dane z pliku CSV.
# Założenia:
#   - parametry: nazwa pliku, encoding, separator
#   - wyjście: lista krotek; każda krotka = linia z pliku


# pliki i katalogi - przeglądanie
