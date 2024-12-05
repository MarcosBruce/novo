from flask import Flask, render_template, request, redirect, url_for, flash

# Inicializando o Flask
app_Marcos = Flask(__name__)
app_Marcos.secret_key = 'sua_chave_secreta'  # Necessário para usar mensagens flash

# Rota principal (raiz)
@app_Marcos.route('/')
def raiz():
    return render_template('index.html')

# Rota para a tela de login
@app_Marcos.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        senha = request.form['password']
        if validar_senha(senha):
            flash('Login realizado com sucesso!', 'success')
            return redirect(url_for('sucesso'))
        else:
            flash('A senha não atende aos requisitos!', 'error')
    return render_template('login.html')

# Rota para a página de cadastro
@app_Marcos.route('/criar-conta', methods=['GET', 'POST'])
def criar_conta():
    if request.method == 'POST':
        senha = request.form['senha']
        confirmacao = request.form['confirmar_senha']
        if senha != confirmacao:
            flash('As senhas não coincidem!', 'error')
        elif not validar_senha(senha):
            flash('A senha não atende aos requisitos!', 'error')
        else:
            flash('Cadastro realizado com sucesso!', 'success')
            return redirect(url_for('login'))
    return render_template('criar_conta.html')

# Rota para a página de sucesso
@app_Marcos.route('/sucesso')
def sucesso():
    return render_template('sucesso.html')

# Função para validar a senha
def validar_senha(senha):
    import re
    # Requisitos: 6 dígitos, 1 maiúscula, 1 número, 1 caractere especial
    pattern = r'^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{6,}$'
    return bool(re.match(pattern, senha))

# Executando o servidor
if __name__ == '__main__':
    app_Marcos.run(debug=True)
# Configuração inicial do projeto Flask