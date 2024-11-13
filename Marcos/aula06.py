from flask import Flask, render_template

app_Marcos = Flask(__name__)

@app_Marcos.route("/usuario")
def dados_usuario():
    nome_usuario="Mariela"
    dados_usu = {"profissao": "Professora EBTT", "disciplina": "Desenvolvimento Web III"}
    return render_template("usuario.html", nome = nome_usuario,dados = dados_usu)

@app_Marcos.route("/usuarios/<nome_usuario>;<nome_profissao>")
def usuario(nome_usuario, nome_profissao):
    nome_usuario="Mariela"
    dados_usu = {"profissao": nome_profissao, "disciplina": "Desenvolvimento Web III"}
    return render_template("usuario.html", nome = nome_usuario,dados = dados_usu)


@app_Marcos.route("/")
def homepage():
    return render_template ("homepage.html")

@app_Marcos.route("/contato")
def contato():
    return render_template("contato.html")

@app_Marcos.route('/<id>')
def saudacao(id):
    return render_template('homepage_nome.html', nome = id)

if __name__ == "__main__":
    app_Marcos.run(debug=True)