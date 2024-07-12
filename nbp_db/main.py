import sqlalchemy as sa
from sqlalchemy import text
from utils.config import get_config
from utils.db import generate_connection_string
from utils.nbp import get_month_rates

# zapisanie listy słowników do bazy danych:
# 1. połączenie do bazy
# 1a. zbudowanie connection stringa
# 1a'. pobranie konfiguracji
# 1b. podłączenie -> db_connection
# 2. zapisanie samych danych
# 2a. zdefiniowanie tabeli w bazie:
# CREATE TABLE nbp (
#     "data" VARCHAR(12),
#     "CHF" FLOAT,
#     "EUR" FLOAT,
#     "GBP" FLOAT,
#     "USD" FLOAT
# );
# 2b. zasilenie tabeli
# 3. odłączenie się od bazy


def main():
    # baza w sqlite
    # config = get_config("db_config_sqlite.yaml")
    # db_conn_str = generate_connection_string(config, "sqlite")

    # baza w postgresql:
    config = get_config("db_config_lukasz.yaml")
    db_conn_str = generate_connection_string(config, "postgresql")
    db_engine = sa.engine.create_engine(db_conn_str)
    db_connection = db_engine.connect()

    for m in range(1, 8):
        lista_notowan = get_month_rates(m, 2024)

        # wywołanie zapytania SQL
        sql_query = 'INSERT INTO nbp (data, "CHF", "EUR", "GBP", "USD") VALUES (:data, :CHF, :EUR, :GBP, :USD)'
        db_connection.execute(text(sql_query), lista_notowan)
        db_connection.commit()

    # rozłączenie od bazy
    db_connection.close()


if __name__ == "__main__":
    main()
