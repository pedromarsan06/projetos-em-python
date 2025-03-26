from main import app
@app.route("/")
def homepage():
    return "SEJA BEM VINDO AO APP EM PYTHON"
@app.route("/repos")
def repos():
    return "Meus repos: https://www.github.com/pedromarsan06"