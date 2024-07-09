import csv


# Funkcja do wczytywania danych z pliku CSV
def wczytaj_dane(plik):
    with open(plik, "r", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=";")
        dane = list(reader)
    return dane


# Funkcja do sortowania danych po wadze
def sortuj_po_wadze(dane):
    # Zamieniamy wagi na liczby całkowite i sortujemy malejąco
    return sorted(dane, key=lambda x: int(x[3]), reverse=True)


# Funkcja do wyświetlania danych
def wyswietl_dane(dane):
    for rekord in dane:
        print(";".join(rekord))


# Główna funkcja programu
def main():
    plik = "bmi.csv"
    dane = wczytaj_dane(plik)
    dane_posortowane = sortuj_po_wadze(dane)
    wyswietl_dane(dane_posortowane)


if __name__ == "__main__":
    main()
