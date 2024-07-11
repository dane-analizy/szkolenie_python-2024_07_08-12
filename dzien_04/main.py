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

nazwa_pliku = "bmi.csv"
enc = "utf-8"
separator = ";"

lista = [linia.strip().split(separator) for linia in open(nazwa_pliku, encoding=enc)]

for nr, elem in enumerate(lista, start=1):
    imie = elem[0]
    nazwisko = elem[1]
    try:
        wzrost_m = float(elem[2]) / 100
        waga_kg = float(elem[3])
    except ValueError:
        print(f"Błędne dane o wzroście lub wadze dla {imie} {nazwisko} - linia {nr}")
        continue

    bmi = waga_kg / wzrost_m**2
    print(f"BMI dla {imie} {nazwisko} wynosi {bmi:.2f}")


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
