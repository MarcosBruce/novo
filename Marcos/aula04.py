from flask import Flask, render_template

app_Marcos = Flask(__name__ , template_folder='templates')

@app_Marcos.route("/")
def homepage():
    return render_template ("homepage.html")

@app_Marcos.route("/contato")
def contato():
    return render_template("contato.html")

if __name__ == "__main__":
    app_Marcos.run(debug=True)