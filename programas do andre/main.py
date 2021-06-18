# coding: utf-8

from tkinter import *
from decouple import config

import os
import cx_Oracle

os.chdir(config('DRIVE'))
os.chdir(config('DRIVE') + '\\' + config('PATH'))

#OPCAO 1
def cadastreAutor(conexao):
    cursor = conexao.cursor()
    nome = input("\nNome do autor? ")

    try:
        cursor.execute("INSERT INTO Autores (Id,Nome) VALUES (seqAutores.nextval,'" + nome + "')")
        conexao.commit()
        print("Autor cadastrado com sucesso")
    except cx_Oracle.DatabaseError:
        print("Autor repetido")


#OPCAO 2
def removaAutor(conexao):
    cursor = conexao.cursor()
    nome = input("\nNome do autor? ")

    cursor.execute("SELECT Id FROM Autores WHERE Nome='" + nome + "'")
    conexao.commit()

    linha = cursor.fetchone()
    if not linha:
        print("Autor inexistente")
    else:
        cursor.execute("DELETE FROM Autores WHERE Nome='" + nome + "'")
        conexao.commit()
        print("Autor removido com sucesso")

#OPCAO 3
def listeAutor(conexao):
    cursor = conexao.cursor()
    cursor.execute("SELECT Autores.Id, Autores.Nome FROM Autores")

    linha = cursor.fetchone()
    if not linha:
        print("Não há Autores cadastrados")
        return

    while linha:
        print(f"{linha[0]}   {linha[1]}")
        linha = cursor.fetchone()

#OPCAO 4
def cadastreLivro(conexao):
    cursor = conexao.cursor()
    nomeLivro = input("\nNome do livro? ")

    try:
        precoLivro = float(input("Preço do livro? "))
    except ValueError:
        print("Preço inválido")
    else:
        nomeAutor = input("Nome do autor? ")

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
                print("Livro repetido")
            else:
                cursor.execute("SELECT Codigo FROM Livros WHERE Nome='" + nomeLivro + "'")
                linha = cursor.fetchone()
                CodigoLivro = linha[0]

                cursor.execute(
                    "INSERT INTO Autorias (Id,Codigo) VALUES (" + str(idAutor) + "," + str(CodigoLivro) + ")")
                conexao.commit()
                print("Livro cadastrado com sucesso")


#OPCAO 5
def removaLivro(conexao):
    cursor = conexao.cursor()
    nome = input("\nNome do livro? ")

    cursor.execute("SELECT Codigo FROM Livros WHERE Nome='" + nome + "'")
    linha = cursor.fetchone()

    if not linha:
        print("Livro inexistente")
    else:
        CodigoLivro = linha[0]

        cursor.execute("SELECT Id FROM Autorias WHERE Codigo=" + str(CodigoLivro))
        linha = cursor.fetchone()
        idAutor = linha[0]

        cursor.execute("DELETE FROM Autorias WHERE Id=" + str(idAutor))
        cursor.execute("DELETE FROM Livros   WHERE Codigo=" + str(CodigoLivro))
        conexao.commit()

        print("Autor removido com sucesso")

#OPCAO 6
def listeTodosLivros(conexao):
    cursor = conexao.cursor()
    cursor.execute(
        "SELECT Livros.Nome, Autores.Nome, Livros.Preco FROM Livros, Autorias, Autores WHERE Livros.Codigo=Autorias.Codigo AND Autorias.Id=Autores.Id")

    linha = cursor.fetchone()
    if not linha:
        print("Não há livros cadastrados")
        return

    while linha:
        print(linha[0] + " " + linha[1] + " " + str(linha[2]))
        linha = cursor.fetchone()

#OPCAO 7
def liste_livros_ate_preco(conexao):
    try:
        precoLivro = float(input("Listar livros ate quantos R$? "))
    except ValueError:
        print("Preço inválido")

    cursor = conexao.cursor()
    cursor.execute(f"SELECT Livros.Nome, Autores.Nome, Livros.Preco FROM Livros, Autorias, Autores WHERE Livros.Preco <= {precoLivro}")

    # WHERE Livros.Codigo=Autorias.Codigo AND Autorias.Id=Autores.Id")

    linha = cursor.fetchone()
    if not linha:
        print("Não há livros até esse preço")
        return

    while linha:
        print(linha[0] + " " + linha[1] + " " + str(linha[2]))
        linha = cursor.fetchone()

#OPCAO 8
def liste_livros_faixa_preco(conexao):
    cursor = conexao.cursor()
    try:
        preco_min = float(input("Preço mínimo do livro? R$"))
        preco_max = float(input("Preço máximo do livro? R$"))

    except ValueError:
        print("Preço inválido")


    cursor.execute(f"SELECT Livros.Nome, Autores.Nome, Livros.Preco FROM Livros, Autorias, Autores WHERE Livros.Preco >= {preco_min} and Livros.Preco <= {preco_max}")

    # WHERE Livros.Codigo=Autorias.Codigo AND Autorias.Id=Autores.Id")

    linha = cursor.fetchone()
    if not linha:
        print("Não há livros nessa faixa de preço")
        return

    while linha:
        print(linha[0] + " " + linha[1] + " " + str(linha[2]))
        linha = cursor.fetchone()

#OPCAO 9
def liste_livros_acima_preco(conexao):
    try:
        precoLivro = float(input("Listar livros acima de quantos R$? R$"))
    except ValueError:
        print("Preço inválido")

    cursor = conexao.cursor()
    cursor.execute(f"SELECT Livros.Nome, Autores.Nome, Livros.Preco FROM Livros, Autorias, Autores WHERE Livros.Preco >= {precoLivro}")

    # WHERE Livros.Codigo=Autorias.Codigo AND Autorias.Id=Autores.Id")

    linha = cursor.fetchone()
    if not linha:
        print("Não há livros acima desse preço")
        return

    while linha:
        print(linha[0] + " " + linha[1] + " " + str(linha[2]))
        linha = cursor.fetchone()



def main():
    print("PROGRAMA PARA PARA CADASTRAR LIVROS E SEUS AUTORES")

    servidor = config('DB_SERVIDOR')
    usuario = config('DB_USUARIO')
    senha = config('DB_SENHA')

    try:
        conexao = cx_Oracle.connect(dsn=servidor, user=usuario, password=senha)
        cursor = conexao.cursor()
    except cx_Oracle.DatabaseError:
        print("Erro de conexão com o BD\n")
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

    fimDoPrograma = False
    while not fimDoPrograma:
        print("\n1) Cadastrar Autor")
        print("2) REMOVER   Autor")
        print("3) LISTAR    Autor")
        print("4) CADASTRAR Livro")
        print("5) REMOVER   Livro")
        print("6) LISTAR    Todos os Livros")
        print("7) LISTAR    os Livros até certo preço")
        print("8) LISTAR    os Livros numa faixa de preço")
        print("9) LISTAR    os Livros acima de um certo preço")
        print("0) Terminar\n")

        try:
            opcao = int(input("Digite sua opção: "));
        except ValueError:
            print("Opção inválida\n")
        else:
            if opcao == 1:
                cadastreAutor(conexao)
            elif opcao == 2:
                removaAutor(conexao)
            elif opcao == 3:
                listeAutor(conexao)
            elif opcao == 4:
                cadastreLivro(conexao)
            elif opcao == 5:
                removaLivro(conexao)
            elif opcao == 6:
                listeTodosLivros(conexao)
            elif opcao == 7:
                liste_livros_ate_preco(conexao)
            elif opcao == 8:
                liste_livros_faixa_preco(conexao)
            elif opcao == 9:
                liste_livros_acima_preco(conexao)
            elif opcao == 0:
                fimDoPrograma = True
            else:
                print("Opção inválida\n")

    print("\nOBRIGADO POR USAR ESTE PROGRAMA")

# daqui para cima  temos definições de subprogramas
# daqui para baixo temos o programa

main()