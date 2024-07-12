from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("sklep_hp.html")


@app.route("/kontakt")
def kontakt():
    return render_template("sklep_kontakt.html")


@app.route("/onas")
def onas():
    return render_template("sklep_onas.html")


@app.route("/uslugi")
def uslugi():
    return render_template("sklep_uslugi.html")


@app.route("/produkty")
def produkty():
    return render_template("sklep_produkty.html")


if __name__ == "__main__":
    app.run(debug=True)
