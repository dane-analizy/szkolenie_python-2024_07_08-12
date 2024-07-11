def wez_nazwe_pliku():
    return input("Podaj nazwe pliku: ")


def wczytaj_linie(nazwa_pliku, enc):
    return [
        linia.strip()
        for linia in open(nazwa_pliku, "r", encoding=enc)
        if len(linia.strip())
    ]


def podziel_linie(lista_linii, separator):
    return [tuple(linia.split(separator)) for linia in lista_linii]


def daj_czyste_dane_z_pliku(nazwa=None, enc="utf-8", sep=";"):
    if not nazwa:
        # parametr "nazwa" nie został podany, więc zapytaj użytkownika
        nazwa = wez_nazwe_pliku()
    # czy plik o nazwie zawartej w zmiennej "nazwa" istnieje? -> zagadnienie z plików
    dane = wczytaj_linie(nazwa, enc)
    dane_czyste = podziel_linie(dane, sep)
    return dane_czyste
