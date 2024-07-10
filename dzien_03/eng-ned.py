import pandas as pd

nazwa_pliku = "eng-ned.txt"
DRUZYNA_A = "Anglia"
DRUZYNA_B = "Holandia"

# miejsce na liste rozgrywek z wynikami
wyniki = []
for nr_linii, linia in enumerate(open(nazwa_pliku, "r", encoding="utf-8"), start=1):
    linia_clean = linia.strip()

    if nr_linii % 3 or nr_linii == 3:
        continue

    linia_clean_splitted = linia_clean.split("\t")
    wynik = linia_clean_splitted[5]  # wynik w postaci "X:Y coś jeszcze"
    wynik = wynik.split(" ")[0]  # wynik sprowadzony do postaci "X:Y"
    wynik = wynik.split(":")

    temp_dict = {
        "rok": int(linia_clean_splitted[1].split(".")[-1]),  # data / rok
        linia_clean_splitted[3]: int(wynik[0]),  # drużyna A: wynik B
        linia_clean_splitted[6]: int(wynik[1]),  # drużyna B: wynik B
    }

    temp_dict["wygrany"] = (
        DRUZYNA_A if temp_dict[DRUZYNA_A] > temp_dict[DRUZYNA_B] else DRUZYNA_B
    )

    # temp_dict["wygrany"] = DRUZYNA_A if temp_dict[DRUZYNA_A] > temp_dict[DRUZYNA_B] else DRUZYNA_B
    # rownoznaczne z"
    # if temp_dict[DRUZYNA_A] > temp_dict[DRUZYNA_B]:
    #     temp_dict["wygrany"] = DRUZYNA_A
    # else:
    #     temp_dict["wygrany"] = DRUZYNA_B

    # załatanie remisu
    if temp_dict[DRUZYNA_A] == temp_dict[DRUZYNA_B]:
        temp_dict["wygrany"] = "remis"

    # temp_dict = {'rok': 2006, 'Holandia': 1, 'Anglia': 1, 'wygrany': 'remis'}

    wyniki.append(temp_dict)

# print(wyniki)


# ile było meczy?
ile_meczy = len(wyniki)

# ile razy wygrała Anglia?
ile_wygranych_a = sum([1 for r in wyniki if r["wygrany"] == DRUZYNA_A])
# ile razy wygrała Holandia?
ile_wygranych_b = sum([1 for r in wyniki if r["wygrany"] == DRUZYNA_B])
# ile razy padł remis?
ile_wygranych_b = sum([1 for r in wyniki if r["wygrany"] == "remis"])

# ile bramek łącznie zdobyła drużyna A (Anglia)?
ile_goli_a = sum([r[DRUZYNA_A] for r in wyniki])
# ile bramek łącznie zdobyła drużyna B?
ile_goli_b = sum([r[DRUZYNA_B] for r in wyniki])

# wyniki dp tabelki pandas
wyniki_df = pd.DataFrame(wyniki)
print(wyniki_df)

print(f"""
Podsumowanie:
    - rozegrano {ile_meczy} spotkań
    - {DRUZYNA_A} wygrała {ile_wygranych_a} spotkań ({ile_wygranych_a/ile_meczy*100:.1f} %), łącznie zdobywając {ile_goli_a} bramek (średnio {ile_goli_a/ile_meczy:.2f} w meczu)
    - {DRUZYNA_B} wygrała {ile_wygranych_b} spotkań ({ile_wygranych_b/ile_meczy*100:.1f} %), łącznie zdobywając {ile_goli_b} bramek (średnio {ile_goli_b/ile_meczy:.2f} w meczu)
""")
