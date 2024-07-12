import time


import requests

JAKIE_WALUTY = ["GBP", "USD", "EUR", "CHF"]


def get_nbp_table(dzien, miesiac, rok):
    data = f"{rok}-{miesiac:02d}-{dzien:02d}"
    url = f"https://api.nbp.pl/api/exchangerates/tables/a/{data}/?format=json"

    notowania = {"data": data, "error": False}

    try:
        time.sleep(0.1)
        res = requests.get(url)
    except Exception as e:
        print(f"Błąd zapytania o {url}: {e}")
        notowania["error"] = True
        return notowania

    if res.status_code != 200:
        print(f"Błąd zapytania o {url}: status HTTP: {res.status_code}")
        notowania["error"] = True
        return notowania

    dane_nbp_lista_kwotowan = res.json()[0]["rates"]

    for kwotowanie in dane_nbp_lista_kwotowan:
        if kwotowanie["code"] in JAKIE_WALUTY:
            notowania[kwotowanie["code"]] = kwotowanie["mid"]

    return notowania


def get_month_rates(miesiac=6, rok=2024):
    lista_notowan = []
    for dzien in range(1, 31):
        notowanie = get_nbp_table(dzien=dzien, miesiac=miesiac, rok=rok)
        if not notowanie["error"]:
            lista_notowan.append(notowanie)

    return lista_notowan


def wypisz_notowania(lista):
    for notowanie in lista:
        print(f"{notowanie['data']}:")
        for waluta in sorted(JAKIE_WALUTY):
            print(f"\t{waluta} = {notowanie[waluta]}")


def main():
    print("\033c", end="")

    lista_notowan = get_month_rates(6, 2024)
    wypisz_notowania(lista_notowan)


if __name__ == "__main__":
    main()
