from flask import Flask, render_template 

app_Marcos = Flask(__name__, template_folder='t_templates')

@app_Marcos.route("/")
@app_Marcos.route("/index")
def indice():
    return render_template("t_index.html")

@app_Marcos.route("/contato")
def contato():
    return render_template("t_contato.html")

@app_Marcos.route("/usuario", defaults={"nome_usuario":"usuário?","nome_profissao":""})
def usuarios (nome_usuario, nome_profissao):
    dados_usu = {"profissao": nome_profissao, "disciplina":"Desenvolvimento Web III"}
    return render_template("t_usuario.html", nome=nome_usuario, dados = dados_usu)

if __name__ == "__main__":
    app_Marcos.run(port=8000)