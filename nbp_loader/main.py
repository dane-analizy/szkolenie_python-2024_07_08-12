import requests

JAKIE_WALUTY = ["GBP", "USD", "EUR", "CHF"]

print("\033c", end="")


def get_nbp_table(dzien, miesiac=6, rok=2024):
    data = f"{rok}-{miesiac:02d}-{dzien:02d}"
    url = f"https://api.nbp.pl/api/exchangerates/tables/a/{data}/?format=json"

    notowania = {"data": data, "error": False}

    try:
        res = requests.get(url)
    except Exception as e:
        print(f"Błąd zapytania o {url}: {e}")
        notowania["error"] = True
        return notowania

    if res.status_code != 200:
        print(f"Błąd zapytania o {url}: status HTTT: {res.status_code}")
        notowania["error"] = True
        return notowania

    dane_nbp_lista_kwotowan = res.json()[0]["rates"]

    for kwotowanie in dane_nbp_lista_kwotowan:
        if kwotowanie["code"] in JAKIE_WALUTY:
            notowania[kwotowanie["code"]] = kwotowanie["mid"]

    return notowania


lista_notowan = []
for dzien in range(1, 31):
    notowanie = get_nbp_table(dzien=dzien)
    if not notowanie["error"]:
        lista_notowan.append(notowanie)


print(lista_notowan)
