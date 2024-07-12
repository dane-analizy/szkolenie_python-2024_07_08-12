import sqlalchemy as sa
from flask import Flask, render_template
from sqlalchemy import text
from utils.config import get_config
from utils.db import generate_connection_string

app = Flask(__name__)

# baza w postgresql:
config = get_config("db_config_lukasz.yaml")
db_conn_str = generate_connection_string(config, "postgresql")
db_engine = sa.engine.create_engine(db_conn_str)


def wez_walute_z_bazy(waluta, data_od):
    sql_query = f'SELECT data, "{waluta}" FROM nbp WHERE data >= :data_od'

    db_connection = db_engine.connect()
    db_results = db_connection.execute(text(sql_query), {"data_od": data_od})
    db_connection.close()

    list_of_results = [{"data": row[0], "kurs": row[1]} for row in db_results]
    return list_of_results


@app.route("/kurs/<waluta>/<od>")
def kwotowania(waluta, od):
    waluta = waluta.upper()
    wyniki = wez_walute_z_bazy(waluta, od)
    return render_template("waluty.html", waluta=waluta, notowania=wyniki)


@app.route("/kurs_json/<waluta>/<od>")
def kwotowania_json(waluta, od):
    waluta = waluta.upper()
    wyniki = wez_walute_z_bazy(waluta, od)
    return wyniki


if __name__ == "__main__":
    app.run()
    # print(wez_walute_z_bazy("EUR", "2024-07-01"))
