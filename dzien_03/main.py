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


# jsony - zapis i odczyt

# # wczytanie konfiguracji
# nazwa_pliku = "konfiguracja.txt"
# nazwa_pliku_config = "konfiguracja.json"
# enc = "utf-8"
# sep = "="
# config = {
#     linia.strip().split(sep)[0]: linia.strip().split(sep)[1]
#     for linia in open(nazwa_pliku, "r", encoding=enc)
# }
# print(config)

# # zapis słownika do pliku JSON
# import json

# with open(nazwa_pliku_config, "w", encoding=enc) as f:
#     json.dump(config, f)


# wczytanie konfiguracji z pliku JSON
# nazwa_pliku_config = "konfiguracja.json"
# enc = "utf-8"

# # zapis słownika do pliku JSON
# import json

# with open(nazwa_pliku_config, "r", encoding=enc) as f:
#     config = json.load(f)

# print(config)
# for k,v in config.items():
#     print(k, v, type(v))


# d = {
#     "login": "jakis_login",
#     "haslo": "tajneHas\u0142o",
#     "baza_danych": 12415,
#     "nowe_parametry": 45.678,
#     "dzien": "środa",
#     "slownik": {"klucza": "a", "kluczb": 124},
# }

# co_zwraca = json.dumps(d)
# print(type(co_zwraca))
# print(co_zwraca)

# slownik -> json.dumps(slownik) -> string z danymi w formie json -> json.dumps(plik) -> string zapisany do pliku


# bmi na slownikach + zapis do jsona

### ZADANIE

# Wczytaj dane z pliku bmi.csv i utwórz z nich słownik.
# Kluczem niech będzie krotka stworzona z imienia i nazwiska,
# a wartością lista stworzona z wagi i wzrostu.
# Wyświetl kolejne elementy słownika w konsoli.
# Zapisz słownik do pliku JSON - np. bmi.json


# open("bmi.csv") + split
# d = {
#       (imie, nazwisko) : [waga, wzrost ],
#       (imie, nazwisko) : [waga, wzrost ]
#     }
# json.dump(d, plik.json)

# rozwiązanie długie
# nazwa_pliku = "bmi.csv"
# nazwa_pliku_bmi = "bmi.json"
# enc, sep = ("utf-8", ";")

# zawartosc_pliku = [
#     linia.strip().split(sep) for linia in open(nazwa_pliku, "r", encoding=enc)
# ]

# print(zawartosc_pliku)

# slownik = {}
# for wiersz in zawartosc_pliku:

#     # # oryginalnie:
#     # slownik[wiersz[0], wiersz[1]] = [wiersz[2], wiersz[3]]
#     # # dodanie explicite że klucz jest krotką:
#     # slownik[(wiersz[0], wiersz[1])] = [wiersz[2], wiersz[3]]
#     # pakiet json nie umie zserializowac klucza-krotki, więc robimy string:
#     slownik[f"{wiersz[0]}-{wiersz[1]}"] = [wiersz[2], wiersz[3]]

# print(slownik)

# import json

# with open(nazwa_pliku_bmi, "w", encoding=enc) as f:
#     json.dump(slownik, f)


# rozwiązanie krótkie
# nazwa_pliku = "bmi.csv"
# nazwa_pliku_bmi = "bmi.json"
# enc, sep = ("utf-8", ";")

# zawartosc_pliku = [
#     linia.strip().split(sep) for linia in open(nazwa_pliku, "r", encoding=enc)
# ]

# # slownik = {}
# # for wiersz in zawartosc_pliku:
# #     slownik[f"{wiersz[0]}-{wiersz[1]}"] = [wiersz[2], wiersz[3]]

# slownik = {
#     f"{wiersz[0]}-{wiersz[1]}": [wiersz[2], wiersz[3]] for wiersz in zawartosc_pliku
# }
# print(slownik)


# jeszcze krótsze - ale czy czytelniejsze?
# nazwa_pliku = "bmi.csv"
# nazwa_pliku_bmi = "bmi.json"
# enc, sep = ("utf-8", ";")

# slownik = {
#     f"{linia.strip().split(sep)[0]}-{linia.strip().split(sep)[1]}": [
#         linia.strip().split(sep)[2],
#         linia.strip().split(sep)[3],
#     ]
#     for linia in open(nazwa_pliku, "r", encoding=enc)
# }

# print(slownik)


### ZADANIE

# Policz ile razy występują poszczególne słowa w tekście "Pana Tadeusza".
# Użyj słowników - kluczem niech będzie słowo zapisane małymi literami, a wartością - liczba jego wystąpień.

# utworzyc slownik liczba_wystapien = {}
# linia po linii pobrac tekst, rozdzielic na slowa, zrobic .lower() i użyc jako klucza
# jesli słowo istniało (d.keys(), d.get()) - zwiekszamy licznik o 1, jesli nie - tworzymy nowe


# rozwiązanie:
# nazwa_pliku = "pan-tadeusz.txt"
# enc = "utf-8"

# zakazane_znaki = ".,?!/()-"

# liczba_wystapien = {}

# for linia in open(nazwa_pliku, "r", encoding=enc):
#     # wyczyczenie całej linii z nieporządanych znakow
#     linia_czysta = linia
#     for znak_zakazany in zakazane_znaki:
#         linia_czysta = linia_czysta.replace(znak_zakazany, " ")

#     # rozbicie linii na slowa
#     slowa_z_linii = linia_czysta.strip().split(" ")

#     # dla kazdego ze slow - dodanie do slownika/zwiekszenie o 1 licznika wystapien
#     for slowo in slowa_z_linii:
#         # tylko "całe" slowa, dłuższe niż 3 znaki
#         if len(slowo) <= 3:
#             continue

#         # klucz mala litera
#         klucz = slowo.lower()
#         # czy juz bylo w slowniku?
#         if klucz in liczba_wystapien.keys():
#             liczba_wystapien[klucz] = liczba_wystapien[klucz] + 1
#         else:
#             liczba_wystapien[klucz] = 1

# # print(liczba_wystapien)


# # posorotwanie słownika - po kluczach (= słowach w tym przypadku) -> dostajemy listę krotek
# # liczba_wystapien_sorted = sorted(liczba_wystapien.items(), key=lambda el: el[0])

# # posorotwanie słownika - po wartościach (= liczbie wystąpień w tym przypadku) -> dostajemy listę krotek
# liczba_wystapien_sorted = sorted(liczba_wystapien.items(), key=lambda el: el[1])


# # rzutowanie listy krotek na słownik - wersja A
# # liczba_wystapien_sorted = dict(liczba_wystapien_sorted)

# # rzutowanie listy krotek na słownik - wersja B
# liczba_wystapien_sorted = {k[0]: k[1] for k in liczba_wystapien_sorted}

# print(liczba_wystapien_sorted)

# rozwiązanie inne:
# nazwa_pliku = "pan-tadeusz.txt"
# enc = "utf-8"
# zakazane_znaki = ".,?!/()-\n"

# # wczytanie całego tekstu
# caly_tekst = open(nazwa_pliku, "r", encoding=enc).read()
# caly_tekst = caly_tekst.lower()

# # oczyszczenie z nieporzadanych znakow
# for znak_zakazany in zakazane_znaki:
#     caly_tekst = caly_tekst.replace(znak_zakazany, " ")

# lista_unikalnych_slow = set(caly_tekst.split(" "))

# liczba_wystapien = {}
# for slowo in lista_unikalnych_slow:
#     if len(slowo) <= 3:
#         continue
#     ile_razy_wystepuje = caly_tekst.count(slowo)
#     liczba_wystapien[slowo] = ile_razy_wystepuje

# # posorotwanie słownika - po wartościach (= liczbie wystąpień w tym przypadku) -> dostajemy listę krotek
# liczba_wystapien_sorted = sorted(liczba_wystapien.items(), key=lambda el: el[1])

# # rzutowanie listy krotek na słownik - wersja B
# liczba_wystapien_sorted = {k[0]: k[1] for k in liczba_wystapien_sorted}

# print(liczba_wystapien_sorted)

from collections import Counter

nazwa_pliku = "pan-tadeusz.txt"
enc = "utf-8"
zakazane_znaki = ".,?!/()-\n"

# wczytanie całego tekstu
caly_tekst = open(nazwa_pliku, "r", encoding=enc).read()
caly_tekst = caly_tekst.lower()

# oczyszczenie z nieporzadanych znakow
for znak_zakazany in zakazane_znaki:
    caly_tekst = caly_tekst.replace(znak_zakazany, " ")


caly_tekst_rozdzielony = caly_tekst.split(" ")
caly_tekst_rozdzielony = [slowo for slowo in caly_tekst_rozdzielony if len(slowo) > 3]

licznik = Counter(caly_tekst_rozdzielony)
print(dict(licznik.most_common(50)))  # 50 najpopularniejszych słów w Panu Tadeuszu
