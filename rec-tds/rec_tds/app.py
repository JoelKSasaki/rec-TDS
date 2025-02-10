from flask import *
import mysql.connector

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/cadastro")
def cadastro():
    return render_template('cadastro.html')

@app.route("/nova-senha")
def newpassword():
    return render_template('novasenha.html')

@app.route("/main")
def inicio():
    return render_template('main.html')

@app.route("/locacao")
def locacao():
    return render_template('locacao.html')
