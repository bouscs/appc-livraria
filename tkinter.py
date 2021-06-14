import os
os.chdir("C:")
os.chdir("C:\\Users\\Shinjo-PC\\Documents\\Downloads\\instantclient-basic-windows.x64-19.6.0.0.0dbru\\instantclient_19_6")

# coding: utf-8
import cx_Oracle

from tkinter import *

#OPCAO 1
def cadastreAutor(conexao):
    cursor = conexao.cursor()
    nome = txtNomeAutor.get() #recupera o que foi digitado na caixa de texto txtNomeAutor

    try:
        cursor.execute("INSERT INTO Autores (Id,Nome) VALUES (seqAutores.nextval,'" + nome + "')")
        conexao.commit()
        lblmsg["text"] = 'Autor cadastrado com sucesso'
    except cx_Oracle.DatabaseError:
        lblmsg["text"] = 'Não foi possivel cadastrar o autor'
    
    txtNome.delete(0,END) #limpa o que estava escrito na caixa de texto txtNome
    '''
        Talvez vai precisar add mais txt.delete(0,end)
    '''


#OPCAO 2
def removaAutor(conexao):
    cursor = conexao.cursor()
    nome = txtNomeAutor.get() #recupera o que foi digitdo na caixa de texto txtNomeAutor

    cursor.execute("SELECT Id, Nome FROM Autores WHERE Nome='" + nome + "'")
    conexao.commit()

    linha = cursor.fetchone()
    if not linha:
        lblmsg["text"] = 'Autor inexistente'
    else:
        cursor.execute("DELETE FROM Autores WHERE Nome='" + nome + "'")
        conexao.commit()
        lblmsg["text"] = 'Autor removido com sucesso'

    txtNomeAutor.delete(0,END) #limpa o que estava escrito na caixa de texto txtNomeAutor


#OPCAO 3
#def listeAutor(conexao):
    
#OPCAO 4
def cadastreLivro(conexao):
    cursor = conexao.cursor()
    nomeLivro = txtNomeLivro.get() #recupera o que foi digitado na caixa de texto txtNomeLivro

    try:
        precoLivro = txtPrecoLivro.get() #recupera o que foi digitado na caixa de texto txtNomeLivro
    except ValueError:
        lblmsg["text"] = 'Preço inválido'
    
    else:
        nomeAutor = txtNomeAutor.get() #recupera o que foi digitado na caixa de texto txtNomeAutor

        cursor.execute("SELECT Id FROM Autores WHERE Nome='" + nomeAutor + "'")
        linha = cursor.fetchone()
        if not linha:
            print("Autor inexistente")
        else:
            idAutor = linha[0]

            try:
                cursor.execute(
                    "INSERT INTO Livros (Codigo,Nome,Preco) VALUES (seqLivros.nextval,'" + nomeLivro + "'," + str(
                        precoLivro) + ")")
                conexao.commit()
            except cx_Oracle.DatabaseError:
                lblmsg["text"] = 'Livro repetido'
            else:
                cursor.execute("SELECT Codigo FROM Livros WHERE Nome='" + nomeLivro + "'")
                linha = cursor.fetchone()
                CodigoLivro = linha[0]

                cursor.execute(
                    "INSERT INTO Autorias (Id,Codigo) VALUES (" + str(idAutor) + "," + str(CodigoLivro) + ")")
                conexao.commit()
                lblmsg["text"] = 'Livro cadastrado com sucesso'


#OPCAO 5
def removaLivro(conexao):
    cursor = conexao.cursor()
    nome = txtNomeLivro.get() #recupera o que foi digitado na caixa de texto txtNomeLivro

    cursor.execute("SELECT Codigo FROM Livros WHERE Nome='" + nome + "'")
    linha = cursor.fetchone()

    if not linha:
        lblmsg["text"] = 'Livro inexistente'
    else:
        CodigoLivro = linha[0]

        cursor.execute("SELECT Id FROM Autorias WHERE Codigo=" + str(CodigoLivro))
        linha = cursor.fetchone()
        idAutor = linha[0]

        cursor.execute("DELETE FROM Autorias WHERE Id=" + str(idAutor))
        cursor.execute("DELETE FROM Livros   WHERE Codigo=" + str(CodigoLivro))
        conexao.commit()
        lblmsg["text"] = 'Livro removido com sucesso'

    txtNomeLivro.delete(0,END) #limpa o que estava escrito na caixa de texto txtNomeAutor

 
    
#OPCAO 6
#def listeTodosLivros(conexao):

#OPCAO 7
#def liste_livros_ate_preco(conexao):

#OPCAO 8
#def liste_livros_faixa_preco(conexao):

#OPCAO 9
#def liste_livros_acima_preco(conexao):






def main():
    print("PROGRAMA PARA PARA CADASTRAR LIVROS E SEUS AUTORES")

    servidor = 'localhost/xe'
    usuario = 'SYSTEM'
    senha = 'aluno'

    try:
        conexao = cx_Oracle.connect(dsn=servidor, user=usuario, password=senha)
        cursor = conexao.cursor()
    except cx_Oracle.DatabaseError:
        lblmsg["text"] = '"Erro de conexão com o BD'
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
        cursor.execute(
            "CREATE TABLE Livros (Codigo NUMBER(5) PRIMARY KEY, Nome NVARCHAR2(50) UNIQUE NOT NULL, Preco NUMBER(5,2) NOT NULL)")
        conexao.commit()
    except cx_Oracle.DatabaseError:
        pass  # ignora, pois a tabela já existe

    try:
        cursor.execute(
            "CREATE TABLE Autorias (Id NUMBER(3), Codigo NUMBER(5), FOREIGN KEY (Id) REFERENCES Autores(Id), FOREIGN KEY (Codigo) REFERENCES Livros(Codigo))")
        conexao.commit()
    except cx_Oracle.DatabaseError:
        pass  # ignora, pois a tabela já existe