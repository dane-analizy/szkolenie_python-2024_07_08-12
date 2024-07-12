# pip install Flask

# polecany tutorial https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

from flask import Flask

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def home():
    return "Jestem stroną główną"


@app.route("/nowa_strona")
def nowa_strona():
    return "Jestem sobie nową stroną"


if __name__ == "__main__":
    app.run(debug=True)


### ZADANIE

# dodaj kilka kolejnych stron do aplikacji Flaskowej
