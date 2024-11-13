from flask import Flask

app_Marcos = Flask (__name__)

@app_Marcos.route('/')
def raiz():
    return 'Olá, turma!'

app_Marcos.run()