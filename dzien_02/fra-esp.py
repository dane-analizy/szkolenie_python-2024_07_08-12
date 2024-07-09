# Czy Hiszpania czy Francja? na podstawie danych historycznych
# dane z https://www.transfermarkt.pl/vergleich/bilanzdetail/verein/3377/gegner_id/3375


# wczytanie danych z pliku
nazwa_pliku = "esp_fra.txt"
nazwa_pliku_clean = "esp_fra.csv"
enc = "utf-8"
lista = [
    tuple(linia.strip().split(";"))
    for linia in open(nazwa_pliku, mode="r", encoding=enc)
]
# podgląd pierwszego rekordu
# print(lista[0])


# ETL - rozbijanie i branie tylko istotnych informacji
lista = [
    (
        record[2].split(".")[-1],  # rok z pełnej daty
        record[4],  # kraj 1
        record[5].split(":")[0],  # liczba branek kraj 1
        record[5].split(":")[1],  # liczba branek kraj 2
        record[6],  # kraj 2
    )
    for record in lista
]
# print(lista[:3])

# ETL - zmiana typów
lista = [
    (
        int(record[0]),  # rzutowanei roku na int
        record[1],
        int(record[2]),  # wynik kraj 1 na int
        int(record[3]),  # wynik kraj 2 na int
        record[4],
    )
    for record in lista
]
# print(lista[:3])


# ETL - zmiana typów
lista_ostateczna = []
for record in lista:
    if record[1] == "Hiszpania":
        record_wynikowy = (
            record[0],  # rok - bez zmian w tym samym miejscu
            record[4],  # Francja pierwsza
            record[3],  # bramki Francji
            record[1],  # Hiszpania druga
            record[2],  # bramki Hiszpanii
        )
    else:
        record_wynikowy = (
            record[0],  # rok - bez zmian w tym samym miejscu
            record[1],  # Francja pierwsza
            record[2],  # bramki Francji
            record[4],  # Hiszpania druga
            record[3],  # bramki Hiszpanii
        )
    lista_ostateczna.append(record_wynikowy)

print(lista_ostateczna[:3])

# zapisanie wyczyszczonych danych do CSV
with open(nazwa_pliku_clean, "w", encoding=enc) as f:
    for record in lista_ostateczna:
        linia_do_zapisu = ";".join(map(str, record))
        f.write(linia_do_zapisu + "\n")


# ile było meczy?
liczba_meczy = len(lista_ostateczna)
print(f"Rozegrano {liczba_meczy} spotkań")

# ile punktów łącznie zdobył każdy z krajów?
bramki_fra = 0
bramki_esp = 0
wygrana_fra = 0
wygrana_esp = 0
remis = 0
for rekord in lista_ostateczna:
    bramki_fra += rekord[2]
    bramki_esp += rekord[4]
    if rekord[2] > rekord[4]:
        wygrana_fra += 1
    elif rekord[2] < rekord[4]:
        wygrana_esp += 1
    else:
        remis += 1


print(f"Łączny wynik:\nFrancja {bramki_fra} : {bramki_esp} Hiszpania")
print(
    f"Średnio na mecz:\nFrancja {bramki_fra/liczba_meczy:.2f} : {bramki_esp/liczba_meczy:.2f} Hiszpania"
)
print(
    f"Statystyka spotkań:\n\tWygrana Francji: {wygrana_fra}\n\tWygrana Hiszpanii: {wygrana_esp}\n\tRemis: {remis}\n"
)

print(f"""Prawdopodobieństwo wyniku:
    Wygrana Francji: {wygrana_fra/liczba_meczy*100:.1f}
    Wygrana Hiszpanii: {wygrana_esp/liczba_meczy*100:.1f}
    Remis: {remis/liczba_meczy*100:.1f}""")
