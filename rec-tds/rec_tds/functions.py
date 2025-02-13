from flask import *
from rec_tds.veiculo import Veiculo
from rec_tds.user import Usuario
import mysql.connector

def conexao_abrir(host, usuario, senha, banco):
    return mysql.connector.connect(host=host, user=usuario, password=senha, database=banco)

def selectveiculos(con):
    cursor = con.cursor(dictionary=True)
    sql = "SELECT * FROM veiculo"
    cursor.execute(sql)
    veiculos = []
    for registro in cursor:
        placa = registro["placa"]
        marca = registro["marca"]
        id = registro["id"]
        tipo = registro["tipo"]
        arcon = registro["arcon"]
        portas = registro["portas"]        
        cambio = registro["cambio"]
        lugares = registro["lugares"]

        veiculo = Veiculo(placa, marca, id, tipo, arcon, portas, cambio, lugares)
        veiculos.append(veiculo)

    return veiculos


def cadastrarveiculo(con, placa, marca, id, tipo, arcon, portas, cambio, lugares):
    cursor = con.cursor()
    print(arcon, type(arcon))
    tem_ar = 0
    if arcon == "S":
        tem_ar = 1
    sql = "INSERT INTO veiculo (placa, marca, id, tipo, arcon, portas, cambio, lugares) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    print("placa=", placa)
    print("marca=", marca)
    print("id=", id)
    print("tipo=", tipo)
    print("arcon=", arcon)
    print("portas=", portas)
    print("cambio=", cambio)
    print("lugares=", lugares)
    cursor.execute(sql, (placa, marca, id, tipo, tem_ar, portas, cambio, lugares))
    con.commit()

def cadastraruser(con, email, nome, sobrenome, senha, datanascimento, funcionario):
    cursor = con.cursor()
    sql = "INSERT INTO pessoa (email, nome, sobrenome, senha, datanascimento, funcionario) VALUES (%s, %s, %s, %s, %s, %s)"
    print("email=", email)
    print("nome=", nome)
    print("sobrenome=", sobrenome)
    print("senha=", senha)
    print("datanascimento=", datanascimento)
    print("funcionario=", funcionario)
    cursor.execute(sql, (email, nome, sobrenome, senha, datanascimento, funcionario))
    con.commit()

def salvarlocacao(con, local_retirada, local_devolucao, data_retirada, data_devolucao, hora_retirada, hora_devolucao):
    cursor = con.cursor()
    sql = "INSERT INTO locacao(local_retirada, local_devolucao, data_retirada, data_devolucao, hora_retirada, hora_devolucao) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(sql, (local_retirada, local_devolucao, data_retirada, data_devolucao, hora_retirada, hora_devolucao))
    con.commit()