from flask import Flask

app = Flask(__name__)

@app.route("/")
def homepage():
    return "SEJA BEM VINDO AO APP EM PYTHON"
@app.route("/repos")
def repos():
    return "Meus repos: https://www.github.com/pedromarsan06"
if __name__ == "__main__":
    app.run()