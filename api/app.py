from flask import Flask, Blueprint, render_template, request, redirect, url_for, flash, session
import psycopg2



main = Blueprint('main', __name__)

# Configurações do banco de dados
def get_db_connection():
    return psycopg2.connect('postgres://default:uiHfXp26DIZk@ep-polished-lake-a41n36g0.us-east-1.aws.neon.tech:5432/verceldb?sslmode=require'
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
         # Armazenar dados do usuário na sessão
        session['id'] = usuario[0]
        session['nome'] = usuario[1]
        session['email'] = usuario[2]
        return True
    else:
        return False

@main.route('/')
def home():
    return render_template('index.html')

@main.route('/login', methods=['GET', 'POST'])
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

@main.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('Logout bem sucedido!', 'success')
    return redirect(url_for('home'))

@main.route('/dashboard')
def dashboard():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('dashboard.html')



