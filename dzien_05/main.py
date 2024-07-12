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
