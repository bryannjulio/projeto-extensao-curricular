from flask import Flask, render_template, request, redirect, url_for, flash, session
import psycopg2
import os

app = Flask(__name__)
app.secret_key = 'admin'

# Configurações do banco de dados
def get_db_connection():
    return psycopg2.connect(
       os.environ.get('CONNECT_DB')
    )

# Função para verificar as credenciais do usuário
def validar_credenciais(email, senha):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM usuarios WHERE email = %s AND senha = %s"
    cursor.execute(query, (email, senha))
    usuario = cursor.fetchone()
    cursor.close()
    conn.close()
    if usuario:
        session['id'] = usuario[0]
        session['nome'] = usuario[1]
        session['email'] = usuario[2]
        return True
    else:
        return False

@app.route('/')
def home():
    return render_template('landing_page.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        
        if validar_credenciais(email, senha):
            session['logged_in'] = True
            flash('Login bem sucedido!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Credenciais inválidas. Por favor, tente novamente.', 'error')

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('Logout bem sucedido!', 'success')
    return redirect(url_for('home'))

@app.route('/dashboard')
def dashboard():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('dashboard.html')

@app.route('/doacao', methods=['POST'])
def doacao():
    nome_do_doador = request.form['nome']
    email_do_doador = request.form['email']
    valor = request.form['valor']
    mensagem = request.form['mensagem']
    
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "INSERT INTO doacoes (nome_do_doador, email_do_doador, valor, mensagem) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (nome_do_doador, email_do_doador, valor, mensagem))
    conn.commit()
    cursor.close()
    conn.close()
    
    flash('Doação realizada com sucesso!', 'success')
    return redirect(url_for('home'))

@app.route('/cadastro_voluntario', methods=['POST'])
def cadastro_voluntario():
    nome = request.form['nome']
    email = request.form['email']
    telefone = request.form['telefone']
    habilidades = request.form['habilidades']
    
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "INSERT INTO voluntarios (nome, email, telefone, habilidades) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (nome, email, telefone, habilidades))
    conn.commit()
    cursor.close()
    conn.close()
    
    flash('Cadastro de voluntário realizado com sucesso!', 'success')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.secret_key = 'admin'
    app.run(debug=True)
