from flask import *
from rec_tds.functions import *
conexao = conexao_abrir("localhost", "root", "joel", "recTDS")

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
    veiculos = selectveiculos(conexao)
    return render_template('main.html', veiculos=veiculos)

@app.route("/locacao")
def locacao():
    return render_template('locacao.html')

@app.route("/cadastro-veiculo")
def veiculo():
    return render_template('cadveiculo.html')

@app.route("/salvarveiculo", methods = ["POST"])
def salvarveiculo():
    placa = request.form.get('placa')
    marca = request.form.get('marca')
    id = request.form.get('id')
    tipo = request.form.get('tipo')
    arcon = request.form.get('arcon')
    ndoors = request.form.get('ndoors') 
    marcha = request.form.get('marcha')
    capacidade = request.form.get('capacidade')

    cadastrarveiculo(conexao, placa, marca, id, tipo, arcon, ndoors, marcha, capacidade)

    return redirect("/main")
