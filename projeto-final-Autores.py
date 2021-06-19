import os
os.chdir("C:")
os.chdir("C:\\Users\\Shinjo-PC\\Documents\\Downloads\\instantclient-basic-windows.x64-19.11.0.0.0dbru\\instantclient_19_11")
# coding: utf-8
import cx_Oracle

from tkinter import *

# OPCAO 0
def buscarAutor(conexao):
    idAutor = txtIdAutor.get()

    cursor = conexao.cursor()
    nomeAutor = cursor.execute(f"SELECT Nome FROM Autores WHERE Id = {idAutor}")
    conexao.commit()

    if not nomeAutor:
        lblmsg["text"] = 'Não foi possivel encontrar o autor'
    else:
        lblmsg["text"] = 'Autor encontrado com sucesso'
        txtNomeAutor.insert(INSERT, nomeAutor)

    txtNomeAutor.delete(0, END)  # limpa o que estava escrito na caixa de texto txtNome
    txtIdAutor.delete(0, END)  # limpa o que estava escrito na caixa de texto txtIdAutor

# OPCAO 1
def cadastreAutor(conexao):
    cursor = conexao.cursor()
    nome = txtNomeAutor.get()  # recupera o que foi digitado na caixa de texto txtNomeAutor

    '''if nome == False:
        lblmsg["text"] = 'Caixa NOME DO AUTOR vazia'
    '''

    try:
        cursor.execute("INSERT INTO Autores (Id,Nome) VALUES (seqAutores.nextval,'" + nome + "')")
        conexao.commit()
        lblmsg["text"] = 'Autor cadastrado com sucesso'
    except cx_Oracle.DatabaseError:
        lblmsg["text"] = 'Não foi possivel cadastrar o autor'

    txtNomeAutor.delete(0, END)  # limpa o que estava escrito na caixa de texto txtNome
    txtIdAutor.delete(0, END)  # limpa o que estava escrito na caixa de texto txtIdAutor


# OPCAO 2
def removaAutor(conexao):
    cursor = conexao.cursor()
    idAutor = txtIdAutor.get()  # recupera o que foi digitdo na caixa de texto txtIdAutor

    cursor.execute(f"SELECT * FROM Autores WHERE Id = {idAutor}")
    conexao.commit()

    linha = cursor.fetchone()
    if not linha:
        lblmsg["text"] = 'Autor inexistente'
    else:
        cursor.execute(f"DELETE FROM Autores WHERE Id = {idAutor}")
        conexao.commit()
        lblmsg["text"] = 'Autor removido com sucesso'

    txtNomeAutor.delete(0, END)  # limpa o que estava escrito na caixa de texto txtNome
    txtIdAutor.delete(0, END)  # limpa o que estava escrito na caixa de texto txtNomeAutor


# OPCAO 3
# def listeAutor(conexao):

def programa():
    servidor = 'localhost/xe'
    usuario = 'SYSTEM'
    senha = 'aluno'

    try:
        conexao = cx_Oracle.connect(dsn=servidor, user=usuario, password=senha)
        cursor = conexao.cursor()
    except cx_Oracle.DatabaseError:
        #lblmsg["text"] = "Erro de conexão com o BD"
        return
    '''
    try:
        cursor.execute("DROP TABLE Autorias")
        conexao.commit()
    except cx_Oracle.DatabaseError:
        pass # ignora, pois a tabela nao existe
    try:
        cursor.execute("DROP SEQUENCE seqAutores")
        conexao.commit()
    except cx_Oracle.DatabaseError:
        pass # ignora, pois a sequencia nao existe
    try:
        cursor.execute("DROP TABLE Autores")
        conexao.commit()
    except cx_Oracle.DatabaseError:
        pass # ignora, pois a tabela nao existe
    try:
        cursor.execute("DROP SEQUENCE seqLivros")
        conexao.commit()
    except cx_Oracle.DatabaseError:
        pass # ignora, pois a sequencia nao existe
    try:
        cursor.execute("DROP TABLE Livros")
        conexao.commit()
    except cx_Oracle.DatabaseError:
        pass # ignora, pois a tabela nao existe
    '''
    try:
        cursor.execute("CREATE SEQUENCE seqAutores START WITH 1 INCREMENT BY 1 MINVALUE 1 MAXVALUE 999 NOCACHE CYCLE")
        conexao.commit()
    except cx_Oracle.DatabaseError:
        pass  # ignora, pois a sequência já existe

    try:
        cursor.execute("CREATE TABLE Autores (Id NUMBER(3) PRIMARY KEY, Nome NVARCHAR2(50) UNIQUE NOT NULL)")
        conexao.commit()
    except cx_Oracle.DatabaseError:
        pass  # ignora, pois a tabela já existe

    try:
        cursor.execute("CREATE SEQUENCE seqLivros START WITH 1 INCREMENT BY 1 MAXVALUE 999 NOCACHE CYCLE")
        conexao.commit()
    except cx_Oracle.DatabaseError:
        pass  # ignora, pois a tabela já existe

    try:
        cursor.execute("CREATE TABLE Livros (Codigo NUMBER(5) PRIMARY KEY, Nome NVARCHAR2(50) UNIQUE NOT NULL, Preco NUMBER(5,2) NOT NULL)")
        conexao.commit()
    except cx_Oracle.DatabaseError:
        pass  # ignora, pois a tabela já existe

    try:
        cursor.execute("CREATE TABLE Autorias (Id NUMBER(3), Codigo NUMBER(5), FOREIGN KEY (Id) REFERENCES Autores(Id), FOREIGN KEY (Codigo) REFERENCES Livros(Codigo))")
        conexao.commit()
    except cx_Oracle.DatabaseError:
        pass  # ignora, pois a tabela já existe


    janela = Tk()

    # ---

    fonte = ("Verdana", "8")

    # ---

    painelDeOrientacao = Frame(janela)
    painelDeOrientacao["pady"] = 10
    painelDeOrientacao.pack()

    titulo = Label(painelDeOrientacao, text="Informe os dados do Autor:")
    titulo["font"] = ("Calibri", "9", "bold")
    titulo.pack()

    # ---

    painelDeBusca = Frame(janela)
    painelDeBusca["padx"] = 20
    painelDeBusca["pady"] = 5
    painelDeBusca.pack()

    lblIdAutor = Label(painelDeBusca, text="Identificacao: ", font=fonte, width=10)
    lblIdAutor.pack(side=LEFT)

    global txtIdAutor
    txtIdAutor = Entry(painelDeBusca)
    txtIdAutor["width"] = 10
    txtIdAutor["font"] = fonte
    txtIdAutor.pack(side=LEFT)

    btnBuscar = Button(painelDeBusca, text="Buscar", font=fonte, width=10)
    btnBuscar["command"] = lambda: buscarAutor(conexao)
    btnBuscar.pack(side=RIGHT)

    # ---

    painelDeNome = Frame(janela)
    painelDeNome["padx"] = 20
    painelDeNome["pady"] = 5
    painelDeNome.pack()

    lblnome = Label(painelDeNome, text="Nome:", font=fonte, width=10)
    lblnome.pack(side=LEFT)

    global txtNomeAutor
    txtNomeAutor= Entry(painelDeNome)
    txtNomeAutor["width"] = 25
    txtNomeAutor["font"] = fonte
    txtNomeAutor.pack(side=LEFT)

    # ---

    painelDeBotoes = Frame(janela)
    painelDeBotoes["padx"] = 20
    painelDeBotoes["pady"] = 10
    painelDeBotoes.pack()

    bntInsert = Button(painelDeBotoes, text="Inserir", font=fonte, width=12)
    bntInsert["command"] = lambda: cadastreAutor(conexao)
    bntInsert.pack(side=LEFT)

    '''bntAlterar = Button(painelDeBotoes, text="Alterar", font=fonte, width=12)
    #bntAlterar["command"] = alterar
    bntAlterar.pack(side=LEFT)'''

    bntExcluir = Button(painelDeBotoes, text="Excluir", font=fonte, width=12)
    bntExcluir["command"] = lambda: removaAutor(conexao)
    bntExcluir.pack(side=LEFT)

    # ---

    painelDeMensagens = Frame(janela)
    painelDeMensagens["pady"] = 15
    painelDeMensagens.pack()

    global lblmsg
    lblmsg = Label(painelDeMensagens, text="Mensagem: ")
    lblmsg["font"] = ("Verdana", "9", "italic")
    lblmsg.pack()

    # ---

    janela.mainloop()


programa()