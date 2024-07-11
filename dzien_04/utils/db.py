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
