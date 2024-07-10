# czyszczenie terminala, odpowiednik Ctrl-L
print("\033c", end="")

### ===========

# napis = "abc"
# print(napis * 5)

# lista = [1, 2, 3]
# print(lista * 5)

# import numpy as np

# wektor = np.array(lista)
# print(wektor, type(wektor))
# print(wektor * 4)
# print(wektor + np.array([3, 2, 1]))

# print("=" * 80)

# słowniki - dict
# para klucz - wartośc
# slownik = {
#     "klucz_jeden": "wartosc",
#     "klucz_dwa": 123,
# }

# print(slownik)


# slownik = {
#     "Klucz_jeden": "Wartość",
#     "Klucz_jeden": 123,
#     "Klucz_jeden": "Wartość inna",
# }

# print(slownik)

# co może by wartością? wszystko
# slownik = {
#     "klucz_str": "wartosc",
#     "klucz_int": 123,
#     "klucz_float": 1.23,
#     "klucz_lista": [1, 2, "abc"],
#     "klucz_krotka": (1, 2, "abc"),
#     "klucz_slownik": {
#         "klucz_jeden": "wartosc",
#         "klucz_dwa": 123,
#     },
# }
# print(slownik)

# mecze = [
#     {
#         "rok": 2020,
#         "drużyna_A": "Francja",
#         "drużyna_B": "Hiszpania",
#         "gole_A": 2,
#         "gole_B": 0,
#         "turniej": "MŚ",
#     },
#     {
#         "rok": 2021,
#         "drużyna_A": "Hiszpania",
#         "drużyna_B": "Francja",
#         "gole_A": 2,
#         "gole_B": 0,
#         "rodzaj_meczu": "towarzyski",
#     },
# ]

# import pandas as pd

# # wczytanie z CSV danych do pandasowego dataframe'a
# # bank = pd.read_csv("konta.csv", sep=";")
# # print(bank.to_dict("records"))

# # utworzenie i wyświetlenie datafrema'e z listy słowników
# mecze_df = pd.DataFrame(mecze)
# print(mecze_df)

# zapianie dataframe'a do CSV
# mecze_df.to_csv("mecze_z_listy_dictow.csv", index=False, sep=";")

# print(pd.DataFrame([slownik]))


# slownik = {
#     "klucz_str": "wartosc",
#     "klucz_int": 123,
#     "klucz_float": 1.23,
#     "klucz_lista": [1, 2, "abc"],
#     "klucz_krotka": (1, 2, "abc"),
#     "klucz_slownik": {
#         "klucz_jeden": "wartosc",
#         "klucz_dwa": 123,
#     },
# }
# sięgamy do słownika pod konkretny klucz:
# print(slownik["klucz_krotka"])

# klucz nie istnieje - błąd:
# print(slownik["klucz_krotka_druga"])

# kluczm moze byc tez krotka
# {
#     (2024, 7, 9): {"temp":30, "opady": 56},
#     (2024, 7, 8): {"temp":30, "opady": 56}
# }


# dane_meteo[(2024, 7, 8)]
# dane_meteo.get( (2024, 7, 8), {} )

# same klucze ze slownika
# print(slownik.keys())

# if "klucz_krotka_druga" in slownik.keys():
#     print(slownik["klucz_krotka_druga"])
# else:
#     print("nie mam pańskiego klucza")

# # dodajemy element do słownika:
# slownik["klucz_krotka_druga"] = "nowy element"

# if "klucz_krotka_druga" in slownik.keys():
#     print(slownik["klucz_krotka_druga"])
# else:
#     print("nie mam pańskiego klucza")

# print(slownik.get("jakis_nieistniejacy_klucz", "wartosc domylsna"))

# slownik["jakis_nieistniejacy_klucz"] = 12345
# print(slownik.get("jakis_nieistniejacy_klucz", "wartosc domylsna"))


# slownik = {}

# print(slownik.get("jakisklucz"))

# if slownik:
#     print("Nie pusty")
# else:
#     print("jedem pustym slownikiem")


# if lista:
#     # lista jest niepusta


# slownik = {
#     "klucz_str": "wartosc",
#     "klucz_int": 123,
#     "klucz_float": 1.23,
#     "klucz_lista": [1, 2, "abc"],
#     "klucz_krotka": (1, 2, "abc"),
#     "klucz_slownik": {
#         "klucz_jeden": "wartosc",
#         "klucz_dwa": 123,
#     },
# }

# same wartości
# print(slownik.values())

# print(slownik.items())

# for klucz, wartosc in slownik.items():
#     print(f"{klucz=} => {wartosc=}")


# # sieganie do zagniezdzonego elementu w slowniku, ktory jest w slowniku
# print(slownik["klucz_slownik"])

# # bezposrednio, ufamy że mamy odpowiednie klucze
# print(slownik["klucz_slownik"]["klucz_jeden"])

# # pewniej i raczej bez bledu:
# print(slownik.get("klucz_slownik", {}).get("klucz_jeden", "nie ma tej wartości"))


# # ale:
# slownik["klucz_slownik"] = 123
# print(slownik.get("klucz_slownik", {}).get("klucz_jeden", "nie ma tej wartości"))


### ZADANIE

# Utwórz plik konfiguracja.txt, który będzie konfiguracją w postaci "klucz=wartość".
# Wczytaj konfigurację do słownika. Wypisz cały słownik.


# rozwiązanie:

# # wczytanie - open()
# nazwa_pliku = "konfiguracja.txt"
# enc = "utf-8"
# sep = "="

# # rozdzielenie linii - split()
# zawartosc_pliku = [
#     linia.strip().split(sep) for linia in open(nazwa_pliku, "r", encoding=enc)
# ]

# print(zawartosc_pliku)


# # budowa słownika
# config = {}
# for wiersz in zawartosc_pliku:
#     config[wiersz[0]] = wiersz[1]

# print(config)

# # wypisanie config.items() w pętli
# for k, v in config.items():
#     print(f"{k}: '{v}'")


# rozwiazanie w krotszej formie:
# wczytanie - open()
# nazwa_pliku = "konfiguracja.txt"
# enc = "utf-8"
# sep = "="

# # rozdzielenie linii - split()
# zawartosc_pliku = [
#     linia.strip().split(sep) for linia in open(nazwa_pliku, "r", encoding=enc)
# ]


# # budowa słownika - dict comprehention
# config = {wiersz[0]: wiersz[1] for wiersz in zawartosc_pliku}

# # wypisanie config.items() w pętli
# for k, v in config.items():
#     print(f"{k}: '{v}'")


# cwieczenie ze slowniak
# jsony - zapis i odczyt
# bmi na slownikach + zapis
