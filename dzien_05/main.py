# czyszczenie terminala, odpowiednik Ctrl-L
print("\033c", end="")

### ===========

# parametryzowanie zapytań do bazy sql

# """
# SELECT
#     region,
#     sklep,
#     SUM(wartosc_sprzedazy) AS suma
# FROM
#     sprzedaz
# WHERE
#     wojewodztwo = "mazowieckie"
#     AND liczba_pracownikow < 10
# GROUP BY
#     region,
#     sklep
# ORDER BY
#     skelp,
#     region
# """


# import sqlalchemy as sa
# from sqlalchemy import text
# from utils.config import get_config
# from utils.db import generate_connection_string

# config = get_config("db_config_lukasz.yaml")
# connection_string = generate_connection_string(config, "postgresql")

# # przygotowanie silnika bazodanowego
# db_engine = sa.engine.create_engine(connection_string)

# # podłączenie do bazy poprzez nasz silnik
# db_connection = db_engine.connect()


# sql_query = """
# SELECT
#     *
# FROM
#     players
# WHERE
#     weight >= :w
#     OR first_name = :imie
# """

# # wywołanie zapytania SQL
# db_results = db_connection.execute(
#     text(sql_query), {"w": 75, "imie": "Marian; SELECT * FROM players;"}
# )

# # nazwy kolumn z zapytania SQL
# db_results_columns = list(db_results.keys())

# # wiersze z zapytania SQL
# list_of_results = [
#     {col[0]: col[1] for col in zip(db_results_columns, row)} for row in db_results
# ]

# for el in list_of_results:
#     print(el)

# # rozłączenie od bazy
# db_connection.close()


# # budowa zapytania przez f-sting

# sql_query = f"""
# SELECT
#     *
# FROM
#     players
# WHERE
#     weight >= {wiek}
#     OR first_name = {imie}
# """


# wkładanie elementów do bazy danych

# import sqlalchemy as sa
# from sqlalchemy import text
# from utils.config import get_config
# from utils.db import generate_connection_string

# config = get_config("db_config_lukasz.yaml")
# connection_string = generate_connection_string(config, "postgresql")

# # przygotowanie silnika bazodanowego
# db_engine = sa.engine.create_engine(connection_string)

# # podłączenie do bazy poprzez nasz silnik
# db_connection = db_engine.connect()

# # insert into players (first_name,last_name,height,weight)
# # values("Jan", "Kowalski", 1.84, 85)
# sql_query = "INSERT INTO players (first_name, last_name, height, weight) VALUES (:imie, :nazwisko, :wzrost, :waga)"

# # wywołanie zapytania SQL
# db_results = db_connection.execute(
#     text(sql_query),
#     [
#         {"imie": "Halina", "nazwisko": "Kowalska-Bąk", "wzrost": 1.65, "waga": 59},
#         {"imie": "Krystyna", "nazwisko": "Góral", "wzrost": 1.71, "waga": 58},
#         {"imie": "Zosia", "nazwisko": "Iksińska", "wzrost": 1.84, "waga": 65},
#         {"imie": "Zły", "nazwisko": "Rekord", "wzrost": "q1.8q4", "waga": 65},
#     ],
# )

# # zakomitowanie zmian w bazie - realne wykonanie insertów
# db_connection.commit()

# # rozłączenie od bazy
# db_connection.close()


# # wkładanie do bazy w paczkach
# for i, rec in enumerate(rekordy):
#     try:
#         db_connection.execute(text("insert into .... () values (:p1, :p2)"), rec)
#     except Exception:
#         print(f"nie udal się insert rekordu {rec}")

#     if i % 10 == 0:
#         db_connection.commit()

# db_connection.commit()



# usługi sieciowe
# API NBP - dokumentacja https://api.nbp.pl/

# potrzebny pakiet requests
# pip install requests

# import requests

# url = "http://api.nbp.pl/api/exchangerates/tables/a/2024-07-01/2024-07-12/?format=json"

# result = requests.get(url)
# print(result)
# print(result.status_code) # HTTP status 
# # print(result.content) # zwrócona zawartość 
# # print(result.text) # zwrócona zawartość jako string

# # żeby dostać słownik z odpowiedzi:
# # json.loads(result.text)
# wynik = result.json()
# print(wynik)


# czy string jest w liście stringów
# if "abc" in ['abc', 'cdf', 'xyz']:
    # "abc" jest na liście


### ZADANIE

# korzystając z API NBP pobierz tabelę kursów z kolejnych dni czerwca 2024 i wyświetl na ekranie kursy GBP, USD, CHF

# Wyswietlamy:

# 2024-06-01:
# \t USD = 4.234
# \t CHF = 4.700
#..
# 2024-06-02:
# \t USD = 4.234
# \t CHF = 4.700


# Endpoint - przykładowe zapytanie https://api.nbp.pl/api/exchangerates/tables/a/2024-07-11/?format=json

# struktura odpowiedzi:
# [
#     {
#         "table": "A",
#         "no": "134/A/NBP/2024",
#         "effectiveDate": "2024-07-11",
#         "rates": [
#             {
#                 "currency": "bat (Tajlandia)",
#                 "code": "THB",
#                 "mid": 0.1082
#             },
# ...

#             {
#                 "currency": "SDR (MFW)",
#                 "code": "XDR",
#                 "mid": 5.1940
#             }
#         ]
#     }
# ]
