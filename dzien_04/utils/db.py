import sqlalchemy as sa
from sqlalchemy import text


def generate_connection_string_postgresql(db_config):
    return f"postgresql+psycopg2://{db_config['db_user']}:{db_config['db_pass']}@{db_config['db_host']}:{db_config['db_port']}/{db_config['db_name']}"


def generate_connection_string_sqlite(db_config):
    return f"sqlite:///{db_config['db_file']}"


def generate_connection_string(db_config, db_type="postgresql"):
    if db_type == "postgresql":
        return generate_connection_string_postgresql(db_config)

    if db_type == "sqlite":
        return generate_connection_string_sqlite(db_config)

    print(f"Nie umiem w ten typ bazy danych {db_type}")
    return None


def get_db_data(connection_string, sql_query):
    # przygotowanie silnika bazodanowego
    db_engine = sa.engine.create_engine(connection_string)

    # podłączenie do bazy poprzez nasz silnik
    db_connection = db_engine.connect()

    # wywołanie zapytania SQL
    db_results = db_connection.execute(text(sql_query))

    # nazwy kolumn z zapytania SQL
    db_results_columns = list(db_results.keys())
    # print(db_results_columns)

    # wiersze z zapytania SQL
    list_of_results = [
        {col[0]: col[1] for col in zip(db_results_columns, row)} for row in db_results
    ]

    # rozłączenie od bazy
    db_connection.close()

    return list_of_results
