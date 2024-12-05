from flask import Flask

app_Marcos = Flask (__name__)

@app_Marcos.route('/ola')
def raiz():
    return 'Olá, turma!'

def saudacoes (nome):
    return f'Olá, {nome}'

if __name__ == "__main__":
    app_Marcos.run()
