from utils.config import get_config
from utils.db import generate_connection_string
from utils.nbp import get_month_rates

# wczytanie danych z NBP do listy słowników
# zapisanie listy słowników do bazy danych:
# 1. połączenie do bazy
# 1a. zbudowanie connection stringa
# 1a'. pobranie konfiguracji
# 1b. podłączenie -> db_connection
# 2. zapisanie samych danych
# 3. odłączenie się od bazy
