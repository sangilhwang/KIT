from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Baldur's Gate 3 2023 GOTY!</h1>"

if __name__ == "__main__":
    app.run()