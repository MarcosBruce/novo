from flask import Flask

app_Marcos = Flask (__name__)

@app_Marcos.route('/')
@app_Marcos.route('/rota1')

def rota1():
    return 'Olá, turma!'

@app_Marcos.route('/rota2')
def rota2():
    resposta = "<H3> Essa é outra página da rota 2 <H3>"
    return resposta

def saudacoes (nome):
    return f'Olá, {nome}'

if __name__ == "__main__":
    app_Marcos.run(debug=True)