from flask import Flask, render_template

app = Flask(__name__)


lista = [f"element {i:02d} w kolejności" for i in range(1, 100)]
zmienna = "ala ma kota"


@app.route("/")
def home():
    return render_template("tabelka.html", nasza_lista=lista, napis=zmienna)


if __name__ == "__main__":
    app.run(debug=True)
