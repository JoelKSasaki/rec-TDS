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

@app.route("/salvarusuario", methods = ["POST"])
def salvarusuario():
    nome = request.form.get('name')
    sobrenome = request.form.get('surname')
    email = request.form.get('newemail')
    createsenha = request.form.get('createsenha')
    confirmsenha = request.form.get('confirmsenha')
    datanascimento = request.form.get('nascimento')
    funcionario = request.form.get('funcionario')

    '''if createsenha != confirmsenha:
        flash("As senhas precisam ser iguais")
        return redirect("/cadastro")
    
    if nome == "" or sobrenome == "" or email == "" or createsenha == "" or confirmsenha == "" or datanascimento == "":       
        flash("Todos os campos são obrigatórios")
        return redirect("/cadastro")'''
    
    cadastraruser(conexao, nome, sobrenome, email, createsenha, datanascimento, funcionario)
    
    return redirect("/login")


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

@app.route("/concluirlocacao")
def concluirlocacao():
    
    return redirect("/main")

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
