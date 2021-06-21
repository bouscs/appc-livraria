from tkinter import *

root = Tk()

inicioPrograma = Frame(root)
inicioPrograma["pady"] = 10
inicioPrograma.pack()

titulo = Label(inicioPrograma, text="Bem vindo ao programa da Livraria")
titulo["font"] = ("Calibri", "12", "bold")
titulo.pack()

def abrirAutores():
    import os
    os.chdir("C:")
    os.chdir(
        "C:\\Users\\Shinjo-PC\\Documents\\Downloads\\instantclient-basic-windows.x64-19.11.0.0.0dbru\\instantclient_19_11")

    # coding: utf-8
    import cx_Oracle



    def limpar():
        listBoxAutores.delete(0, END)
        txtIdAutor.delete(0, END)
        txtNomeAutor.delete(0, END)
        lblmsg["text"] = 'Caixas de entradas limpadas com sucesso'

    # OPCAO 0
    def buscarAutor(conexao):
        idAutor = txtIdAutor.get()

        cursor = conexao.cursor()
        cursor.execute(f"SELECT Nome FROM Autores WHERE Id = {idAutor}")
        nomeAutor = cursor.fetchone()
        conexao.commit()

        if not nomeAutor:
            lblmsg["text"] = 'Não foi possivel encontrar o autor'
        else:
            lblmsg["text"] = 'Autor encontrado com sucesso'
            txtNomeAutor.insert(END, f"{nomeAutor}")


    # OPCAO 1
    def cadastreAutor(conexao):
        cursor = conexao.cursor()
        nome = txtNomeAutor.get()

        try:
            cursor.execute(f"INSERT INTO Autores (Id,Nome) VALUES (seqAutores.nextval,'{nome}')")
            conexao.commit()
            lblmsg["text"] = 'Autor cadastrado com sucesso'
        except cx_Oracle.DatabaseError:
            lblmsg["text"] = 'Não foi possivel cadastrar o autor'

    # OPCAO 2
    def removaAutor(conexao):
        cursor = conexao.cursor()
        idAutor = txtIdAutor.get()

        cursor.execute(f"SELECT * FROM Autores WHERE Id = {idAutor}")
        conexao.commit()

        linha = cursor.fetchone()
        if not linha:
            lblmsg["text"] = 'Autor inexistente'
        else:
            cursor.execute(f"DELETE FROM Autores WHERE Id = {idAutor}")
            conexao.commit()
            lblmsg["text"] = 'Autor removido com sucesso'

    def listeAutor(conexao):
        cursor = conexao.cursor()
        cursor.execute("SELECT Autores.Id, Autores.Nome FROM Autores ORDER BY Id")

        linha = cursor.fetchone()
        if not linha:
            lblmsg["text"] = "Não há Autores cadastrados"
            return
        else:
            while linha:
                assert isinstance(linha, object)
                lblmsg["text"] = "Autores listados com sucesso"
                listBoxAutores.insert(END, f"{linha[0]}   {linha[1]}\n")
                linha = cursor.fetchone()

    def programa():
        servidor = 'localhost/xe'
        usuario = 'SYSTEM'
        senha = 'aluno'

        try:
            conexao = cx_Oracle.connect(dsn=servidor, user=usuario, password=senha)
            cursor = conexao.cursor()
        except cx_Oracle.DatabaseError:
            # lblmsg["text"] = "Erro de conexão com o BD"
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
            cursor.execute(
                "CREATE SEQUENCE seqAutores START WITH 1 INCREMENT BY 1 MINVALUE 1 MAXVALUE 999 NOCACHE CYCLE")
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

        janela = Tk()

        # ---
        janela.geometry("500x500")
        janela.title("Autores")
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
        painelDeBusca["padx"] = 30
        painelDeBusca["pady"] = 5
        painelDeBusca.pack()

        lblIdAutor = Label(painelDeBusca, text="Identificacao: ", font=fonte, width=12)
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
        txtNomeAutor = Entry(painelDeNome)
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

        bntExcluir = Button(painelDeBotoes, text="Excluir", font=fonte, width=12)
        bntExcluir["command"] = lambda: removaAutor(conexao)
        bntExcluir.pack(side=LEFT)

        bntListar = Button(painelDeBotoes, text="Listar", font=fonte, width=12)
        bntListar["command"] = lambda: listeAutor(conexao)
        bntListar.pack(side=LEFT)

        bntLimpar = Button(painelDeBotoes, text="Limpar todas as caixas", font=fonte, width=20)
        bntLimpar["command"] = lambda: limpar()
        bntLimpar.pack(side=BOTTOM)

        # ---

        painelDeMensagens = Frame(janela)
        painelDeMensagens["pady"] = 15
        painelDeMensagens.pack()

        global lblmsg
        lblmsg = Label(painelDeMensagens, text="Mensagem: ")
        lblmsg["font"] = ("Verdana", "9", "italic")
        lblmsg.pack()

        # ---

        painelDeLista = Frame(janela)
        painelDeLista["pady"] = 15
        painelDeLista.pack()

        global listBoxAutores
        listBoxAutores = Listbox(painelDeLista)
        listBoxAutores["font"] = ("Verdana", "9", "italic")
        listBoxAutores.pack()

        janela.mainloop()

    programa()

def abrirLivros():
    import os

    os.chdir("C:")
    os.chdir(
        "C:\\Users\\Shinjo-PC\\Documents\\Downloads\\instantclient-basic-windows.x64-19.11.0.0.0dbru\\instantclient_19_11")
    # coding: utf-8
    import cx_Oracle

    # Função que limpa as caixinhas
    def limpar1():
        txtCodigoLivro.delete(0, END)
        txtNomeLivro.delete(0, END)
        txtPrecoLivro.delete(0, END)
        txtNomeAutorLivro.delete(0, END)
        lblmsg1["text"] = 'Caixas de entradas limpadas com sucesso'

    def limpar2():
        listBox.delete(0, END)
        txtListar1.delete(0, END)
        txtListar2.delete(0, END)
        txtListar3Min.delete(0, END)
        txtListar3Max.delete(0, END)
        lblmsg2["text"] = 'Caixas de entradas limpadas com sucesso'


    # OPCAO 0
    def buscarLivro(conexao):
        codigoLivro = txtCodigoLivro.get()

        cursor = conexao.cursor()
        cursor.execute(
            f"SELECT Livros.Nome, Livros.Preco, Autores.Nome FROM Livros, Autorias, Autores WHERE Livros.Codigo = {codigoLivro} AND Autorias.Codigo = {codigoLivro} AND Autorias.Id=Autores.Id")
        dadosLivro = cursor.fetchone()
        conexao.commit()

        if not dadosLivro:
            lblmsg1["text"] = 'Não foi possivel encontrar o Livro'
        else:
            lblmsg1["text"] = 'Livro encontrado com sucesso'

            txtNomeLivro.insert(END, f"{dadosLivro[0]}")
            txtPrecoLivro.insert(END, f"{dadosLivro[1]}")
            txtNomeAutorLivro.insert(END, f"{dadosLivro[2]}")

    # OPCAO 1 - 4
    def cadastreLivro(conexao):
        cursor = conexao.cursor()
        nomeLivro = txtNomeLivro.get()
        try:
            precoLivro = txtPrecoLivro.get()
        except ValueError:
            lblmsg1["text"] = 'Preço inválido'
        else:
            nomeAutor = txtNomeAutorLivro.get()
            cursor.execute(f"SELECT Id FROM Autores WHERE Nome='{nomeAutor}'")
            linha = cursor.fetchone()
            if not linha:
                print("Autor inexistente")
            else:
                idAutor = linha[0]
                try:
                    cursor.execute(
                        f"INSERT INTO Livros (Codigo,Nome,Preco) VALUES (seqLivros.nextval,'{nomeLivro}',{precoLivro})")
                    conexao.commit()
                except cx_Oracle.DatabaseError:
                    lblmsg1["text"] = 'Livro repetido'
                else:
                    cursor.execute(f"SELECT Codigo FROM Livros WHERE Nome='{nomeLivro}'")
                    linha = cursor.fetchone()
                    codigoLivro = linha[0]
                    cursor.execute(f"INSERT INTO Autorias (Id,Codigo) VALUES ({idAutor}, {codigoLivro})")
                    conexao.commit()
                    lblmsg1["text"] = 'Livro cadastrado com sucesso'

    # OPCAO 2 - 5
    def removaLivro(conexao):
        cursor = conexao.cursor()
        nomeLivro = txtNomeLivro.get()  # recupera o que foi digitado na caixa de texto txtNomeLivro
        cursor.execute(f"SELECT Codigo FROM Livros WHERE Nome='{nomeLivro}'")
        linha = cursor.fetchone()

        if not linha:
            lblmsg1["text"] = 'Livro inexistente'
        else:
            codigoLivro = linha[0]
            cursor.execute(f"SELECT Id FROM Autorias WHERE Codigo={codigoLivro}")
            linha = cursor.fetchone()
            idAutor = linha[0]
            cursor.execute(f"DELETE FROM Autorias WHERE Id= {idAutor}")
            cursor.execute(f"DELETE FROM Livros   WHERE Codigo= {codigoLivro}")
            conexao.commit()
            lblmsg1["text"] = 'Livro removido com sucesso'

    # - opcoes de listagem

    # OPCAO 3 - 6
    def listeTodosLivros(conexao):
        cursor = conexao.cursor()
        cursor.execute(
            "SELECT Livros.Codigo, Livros.Nome, Autores.Nome, Livros.Preco FROM Livros, Autorias, Autores WHERE Livros.Codigo=Autorias.Codigo AND Autorias.Id=Autores.Id")

        linha = cursor.fetchone()
        if not linha:
            lblmsg2["text"] = "Não há Livros cadastrados"
            return
        else:
            while linha:
                assert isinstance(linha, object)
                lblmsg2["text"] = "Livros listados com sucesso"
                listBox.insert(END, f"Codigo: {linha[0]}\n")
                listBox.insert(END, f"Livro: {linha[1]}\n")
                listBox.insert(END, f"Autor: {linha[2]}\n")
                listBox.insert(END, f"Preço: {linha[3]}\n")
                listBox.insert(END, f"\n")
                linha = cursor.fetchone()

    # OPCAO 4 - 7
    def liste_livros_ate_preco(conexao):
        cursor = conexao.cursor()

        try:
            precoLivro = txtListar1.get()
        except ValueError:
            lblmsg2["text"] = "Preço inválido"

        cursor.execute(
            f"SELECT Livros.Preco, Livros.Codigo, Livros.Nome, Autores.Nome FROM Livros, Autorias, Autores WHERE Livros.Codigo=Autorias.Codigo AND Autorias.Id=Autores.Id AND Livros.Preco <= {precoLivro} ORDER BY Livros.Preco")
        linha = cursor.fetchone()
        if not linha:
            lblmsg2["text"] = "Não há Livros abaixo desse preço"
            return
        else:
            while linha:
                assert isinstance(linha, object)
                lblmsg2["text"] = "Livros listados com sucesso"
                listBox.insert(END, f"Preço: {linha[0]}\n")
                listBox.insert(END, f"Codigo: {linha[1]}\n")
                listBox.insert(END, f"Livro: {linha[2]}\n")
                listBox.insert(END, f"Autor: {linha[3]}\n")
                listBox.insert(END, f"\n")
                linha = cursor.fetchone()

    # OPCAO 5 - 8
    def liste_livros_acima_preco(conexao):
        cursor = conexao.cursor()

        try:
            precoLivro = txtListar2.get()
        except ValueError:
            lblmsg2["text"] = "Preço inválido"

        cursor.execute(
            f"SELECT Livros.Preco, Livros.Codigo, Livros.Nome, Autores.Nome FROM Livros, Autorias, Autores WHERE Livros.Codigo=Autorias.Codigo AND Autorias.Id=Autores.Id AND Livros.Preco >= {precoLivro} ORDER BY Livros.Preco")
        linha = cursor.fetchone()
        if not linha:
            lblmsg2["text"] = "Não há livros acima desse preço"
            return
        else:
            while linha:
                assert isinstance(linha, object)
                lblmsg2["text"] = "Livros listados com sucesso"
                listBox.insert(END, f"Preço: {linha[0]}\n")
                listBox.insert(END, f"Codigo: {linha[1]}\n")
                listBox.insert(END, f"Livro: {linha[2]}\n")
                listBox.insert(END, f"Autor: {linha[3]}\n")
                listBox.insert(END, f"\n")
                linha = cursor.fetchone()

    # OPCAO 6 - 9
    def liste_livros_faixa_preco(conexao):
        cursor = conexao.cursor()
        try:
            precoMin = txtListar3Min.get()
        except ValueError:
            lblmsg2["text"] = "Preço inválido"

        try:
            precoMax = txtListar3Max.get()
        except ValueError:
            lblmsg2["text"] = "Preço inválido"

        cursor.execute(
            f"SELECT Livros.Preco, Livros.Codigo, Livros.Nome, Autores.Nome FROM Livros, Autorias, Autores WHERE Livros.Codigo=Autorias.Codigo AND Autorias.Id=Autores.Id AND Livros.Preco >= {precoMin} AND Livros.Preco <= {precoMax} ORDER BY Livros.Preco")
        linha = cursor.fetchone()
        if not linha:
            lblmsg2["text"] = "Não há livros nessa faixa de preço"
            return
        else:
            while linha:
                assert isinstance(linha, object)
                lblmsg2["text"] = "Livros listados com sucesso"
                listBox.insert(END, f"Preço: {linha[0]}\n")
                listBox.insert(END, f"Codigo: {linha[1]}\n")
                listBox.insert(END, f"Livro: {linha[2]}\n")
                listBox.insert(END, f"Autor: {linha[3]}\n")
                listBox.insert(END, f"\n")
                linha = cursor.fetchone()

    def programa():

        servidor = 'localhost/xe'
        usuario = 'SYSTEM'
        senha = 'aluno'

        try:
            conexao = cx_Oracle.connect(dsn=servidor, user=usuario, password=senha)
            cursor = conexao.cursor()
        except cx_Oracle.DatabaseError:
            # lblmsg["text"] = "Erro de conexão com o BD"
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
            cursor.execute(
                "CREATE SEQUENCE seqAutores START WITH 1 INCREMENT BY 1 MINVALUE 1 MAXVALUE 999 NOCACHE CYCLE")
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

        janela = Tk()

        # ---

        fonte = ("Verdana", "8")
        janela.geometry("500x850")
        janela.title("Livros")

        # --- painel orientação

        painelDeOrientacao = Frame(janela)
        painelDeOrientacao["pady"] = 10
        painelDeOrientacao.pack()

        titulo = Label(painelDeOrientacao, text="Informe os dados do livro:")
        titulo["font"] = ("Calibri", "9", "bold")
        titulo.pack()

        # --- painel de busca

        painelDeBusca = Frame(janela)
        painelDeBusca["padx"] = 20
        painelDeBusca["pady"] = 5
        painelDeBusca.pack()

        lblCodLivro = Label(painelDeBusca, text="Código:", font=fonte, width=10)
        lblCodLivro.pack(side=LEFT)

        global txtCodigoLivro
        txtCodigoLivro = Entry(painelDeBusca)
        txtCodigoLivro["width"] = 10
        txtCodigoLivro["font"] = fonte
        txtCodigoLivro.pack(side=LEFT)

        btnBuscar = Button(painelDeBusca, text="Buscar", font=fonte, width=10)
        btnBuscar["command"] = lambda: buscarLivro(conexao)
        btnBuscar.pack(side=RIGHT)

        # --- painel nome livro

        painelDeNome = Frame(janela)
        painelDeNome["padx"] = 20
        painelDeNome["pady"] = 5
        painelDeNome.pack()

        lblnome = Label(painelDeNome, text="Nome Livro:", font=fonte, width=10)
        lblnome.pack(side=LEFT)

        global txtNomeLivro
        txtNomeLivro = Entry(painelDeNome)
        txtNomeLivro["width"] = 25
        txtNomeLivro["font"] = fonte
        txtNomeLivro.pack(side=LEFT)

        # --- Painel preco Livro

        painelPreco = Frame(janela)
        painelPreco["padx"] = 20
        painelPreco["pady"] = 5
        painelPreco.pack()

        lblPreco = Label(painelPreco, text="Preço: R$", font=fonte, width=10)
        lblPreco.pack(side=LEFT)

        global txtPrecoLivro
        txtPrecoLivro = Entry(painelPreco)
        txtPrecoLivro["width"] = 25
        txtPrecoLivro["font"] = fonte
        txtPrecoLivro.pack(side=LEFT)
        # ---

        painelNomeAutor = Frame(janela)
        painelNomeAutor["padx"] = 20
        painelNomeAutor["pady"] = 5
        painelNomeAutor.pack()

        lblNomeAutor = Label(painelNomeAutor, text="Nome Autor", font=fonte, width=10)
        lblNomeAutor.pack(side=LEFT)

        global txtNomeAutorLivro
        txtNomeAutorLivro = Entry(painelNomeAutor)
        txtNomeAutorLivro["width"] = 25
        txtNomeAutorLivro["font"] = fonte
        txtNomeAutorLivro.pack(side=LEFT)

        # --- Mensagem label

        painelDeMensagens1 = Frame(janela)
        painelDeMensagens1["pady"] = 10
        painelDeMensagens1.pack()

        global lblmsg1
        lblmsg1 = Label(painelDeMensagens1, text="Mensagem: ")
        lblmsg1["font"] = ("Verdana", "8", "italic")
        lblmsg1.pack()

        # --- Painel dos botoes

        painelDeBotoes = Frame(janela)
        painelDeBotoes["padx"] = 20
        painelDeBotoes["pady"] = 10
        painelDeBotoes.pack()

        bntInsert = Button(painelDeBotoes, text="Cadastre", font=fonte, width=12)
        bntInsert["command"] = lambda: cadastreLivro(conexao)
        bntInsert.pack(side=LEFT)

        bntExcluir = Button(painelDeBotoes, text="Remover", font=fonte, width=12)
        bntExcluir["command"] = lambda: removaLivro(conexao)
        bntExcluir.pack(side=LEFT)

        bntLimpar = Button(painelDeBotoes, text="Limpar todas as caixas", font=fonte, width=20)
        bntLimpar["command"] = lambda: limpar1()
        bntLimpar.pack(side=BOTTOM)

        # Listagens options

        # --- painel listagem

        painelDeListar = Frame(janela)
        painelDeListar["pady"] = 10
        painelDeListar.pack()

        titulo = Label(painelDeListar, text="Opções de listagem:")
        titulo["font"] = ("Calibri", "9", "bold")
        titulo.pack()

        # --- painel listar 1: f"listar livros até R${X}"

        painelListar1 = Frame(janela)
        painelListar1["padx"] = 1
        painelListar1["pady"] = 1
        painelListar1.pack()

        lblListar1 = Label(painelListar1, text="Listar livros até quantos R$?", font=fonte, width=40)
        lblListar1.pack(side=LEFT)

        global txtListar1
        txtListar1 = Entry(painelListar1)
        txtListar1["width"] = 5
        txtListar1["font"] = fonte
        txtListar1.pack(side=LEFT)

        bntListar1 = Button(painelListar1, text="Listar", font=fonte, width=6)
        bntListar1["command"] = lambda: liste_livros_ate_preco(conexao)
        bntListar1.pack(side=LEFT)

        # --- painel listar 2: f"listar livros acima de quantos R${X}"

        painelListar2 = Frame(janela)
        painelListar2["padx"] = 1
        painelListar2["pady"] = 1
        painelListar2.pack()

        lblListar2 = Label(painelListar2, text="Listar livros acima de quantos R$?", font=fonte, width=40)
        lblListar2.pack(side=LEFT)

        global txtListar2
        txtListar2 = Entry(painelListar2)
        txtListar2["width"] = 5
        txtListar2["font"] = fonte
        txtListar2.pack(side=LEFT)

        bntListar2 = Button(painelListar2, text="Listar", font=fonte, width=6)
        bntListar2["command"] = lambda: liste_livros_acima_preco(conexao)
        bntListar2.pack(side=LEFT)

        # --- painel listar 3: f"listar livros numa faixa de preco"

        painelListar3 = Frame(janela)
        painelListar3["padx"] = 5
        painelListar3["pady"] = 10
        painelListar3.pack()

        lblListar3 = Label(painelListar3, text="Listar livros na faixa de quantos R$?", font=fonte, width=35)
        lblListar3.pack(side=LEFT)

        painelListar3Inputs = Frame(janela)
        painelListar3Inputs["padx"] = 5
        painelListar3Inputs["pady"] = 5
        painelListar3Inputs.pack()

        lblListar3Min = Label(painelListar3Inputs, text="Preco mínimo: R$", font=fonte, width=17)
        lblListar3Min.pack(side=LEFT)

        global txtListar3Min
        txtListar3Min = Entry(painelListar3Inputs)
        txtListar3Min["width"] = 5
        txtListar3Min["font"] = fonte
        txtListar3Min.pack(side=LEFT)

        lblListar3Max = Label(painelListar3Inputs, text="Preco máximo: R$", font=fonte, width=17)
        lblListar3Max.pack(side=LEFT)

        global txtListar3Max
        txtListar3Max = Entry(painelListar3Inputs)
        txtListar3Max["width"] = 5
        txtListar3Max["font"] = fonte
        txtListar3Max.pack(side=LEFT)

        bntListar3 = Button(painelListar3Inputs, text="Listar", font=fonte, width=6)
        bntListar3["command"] = lambda: liste_livros_faixa_preco(conexao)
        bntListar3.pack(side=LEFT)

        # ---

        painelDeMensagens2 = Frame(janela)
        painelDeMensagens2["pady"] = 10
        painelDeMensagens2.pack()

        global lblmsg2
        lblmsg2 = Label(painelDeMensagens2, text="Mensagem: ")
        lblmsg2["font"] = ("Verdana", "8", "italic")
        lblmsg2.pack()

        # ---

        painelDeLista = Frame(janela)
        painelDeLista["padx"] = 100
        painelDeLista["pady"] = 10
        painelDeLista.pack()

        global listBox
        listBox = Listbox(painelDeLista)
        listBox["font"] = ("Verdana", "9", "italic")
        listBox.pack()

        # --- Painel dos botões

        painelDeBotoes = Frame(janela)
        painelDeBotoes["padx"] = 20
        painelDeBotoes["pady"] = 10
        painelDeBotoes.pack()

        bntListar = Button(painelDeBotoes, text="Listar Todos", font=fonte, width=24)
        bntListar["command"] = lambda: listeTodosLivros(conexao)
        bntListar.pack(side=LEFT)

        bntLimpar = Button(painelDeBotoes, text="Limpar todas as caixas", font=fonte, width=20)
        bntLimpar["command"] = lambda: limpar2()
        bntLimpar.pack(side=BOTTOM)
        # ---

        janela.mainloop()

    programa()

btn = Button(root, text="Abrir Sessão de Autores", command=abrirAutores)
btn.pack(padx=30,pady=25, side=LEFT)

btn = Button(root, text="Abrir Sessão de Livros", command=abrirLivros)
btn.pack(padx=30,pady=25, side=LEFT)

root.geometry("400x250")
root.title("Livraria")
root.mainloop()