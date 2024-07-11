# plik startowy - wykorzystuje pakiet utils

# pakiet: UTILS
# moduły: PLIKI, DB, PLOT

from utils.db import zapisz_do_bazy
from utils.pliki import laduj_dane
from utils.plot import wykres_liniowy


def main():
    dane = laduj_dane("plik_z_danymi")
    zapisz_do_bazy(dane)
    wykres_liniowy(dane)


if __name__ == "__main__":
    main()
