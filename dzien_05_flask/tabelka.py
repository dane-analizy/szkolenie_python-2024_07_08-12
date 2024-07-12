from flask import Flask, render_template

app = Flask(__name__)


lista = [f"element {i:02d} w kolejności" for i in range(1, 5)]
zmienna = "ala ma kota"


@app.route("/")
def home():
    return render_template("tabelka.html", nasza_lista=lista, napis=zmienna)


def dodawanie(a, b):
    return a + b


@app.route("/add/<a>/<b>")
def dodaj(a, b):
    a = float(a)
    b = float(b)

    return {"a": a, "b": b, "suma": dodawanie(a, b)}


@app.route("/mult/<a>/<b>")
def iloczyn(a, b):
    a = float(a)
    b = float(b)
    iloczyn = a * b
    return render_template(
        "mnozenie.html", wynik={"czynna": a, "czynnik": b, "mul": iloczyn}
    )


if __name__ == "__main__":
    app.run(debug=True)


### ZADANIE

# Napisz "endpoint" we Flasku, który:
# - przyjmie w adresie 2 liczby
# - policzy ich iloczyn
# - wyświetli liczby oraz wynik korzystając z nowej templatki
