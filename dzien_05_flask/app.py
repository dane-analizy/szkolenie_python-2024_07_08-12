# pip install Flask

# polecany tutorial https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

# from flask import Flask

# app = Flask(__name__)


# @app.route("/")
# @app.route("/index")
# def home():
#     return "Jestem stroną główną"


# @app.route("/nowa_strona")
# def nowa_strona():
#     return "Jestem sobie nową stroną"


# @app.route("/kolejna_strona")
# def kolejna_strona():
#     return "Jestem sobie kolejną stroną"


# if __name__ == "__main__":
#     app.run(debug=True)


### ZADANIE

# Dodaj kilka kolejnych stron do aplikacji Flaskowej


# renredowanie templatek


from flask import Flask, render_template

app = Flask(__name__)


@app.route("/index")
def index():
    return """
<html>

<head>
    <title>Index</title>
</head>

<body>
    <h1>Index</h1>
    <p>To jest jakiś tekst <strong>boldem</strong> i <em>italiciem</em></p>
</body>

</html>
"""


@app.route("/")
def home():
    return render_template("hp.html")


if __name__ == "__main__":
    app.run(debug=True)


### ZADANIE

# Zrób nową stronę w oparciu o template w html
