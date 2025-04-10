
from main import app, render_template

@app.route("/")
def homepage():
    
    return render_template('index.html')
