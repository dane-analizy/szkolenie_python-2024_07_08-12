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

import math

for i in [-2, -1, 0, "a", 1, 2]:
    try:
        wynik = 1 / i
        logarytm = math.log10(i)
    except ZeroDivisionError as e:  # dzielenie przez zero
        print(f"Dzielenie przez zero, {i}: {e}")
    except ValueError as e:  # dzielenie przez błędną wartość
        print(f"Błędna wartość, {i}: {e}")
    except Exception as e:  # każdy inny rodzaj błędu
        print(f"{i}, błąd {e}, {type(e)}")
    print(wynik)
