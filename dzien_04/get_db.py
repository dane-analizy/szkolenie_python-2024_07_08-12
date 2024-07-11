from utils.config import get_config
from utils.db import generate_connection_string, get_db_data

# config = get_config("db_config_lukasz.yaml")
# conn_str = generate_connection_string(config, db_type="postgresql")

config = get_config("db_config_sqlite.yaml")
conn_str = generate_connection_string(config, db_type="sqlite")

sql_query = """
SELECT
    first_name,
    last_name,
    weight / (height * height) AS bmi,
    player_id
FROM
    players
;
"""

list_of_results = get_db_data(conn_str, sql_query)
print(list_of_results)
