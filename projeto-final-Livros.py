from tkinter import *


# OPCAO 4
'''
def cadastreLivro(conexao):
    cursor = conexao.cursor()
    nomeLivro = txtNomeLivro.get()  # recupera o que foi digitado na caixa de texto txtNomeLivro

    try:
        precoLivro = txtPrecoLivro.get()  # recupera o que foi digitado na caixa de texto txtNomeLivro
    except ValueError:
        lblmsg["text"] = 'Preço inválido'

    else:
        nomeAutor = txtNomeAutor.get()  # recupera o que foi digitado na caixa de texto txtNomeAutor

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


# OPCAO 5
def removaLivro(conexao):
    cursor = conexao.cursor()
    nome = txtNomeLivro.get()  # recupera o que foi digitado na caixa de texto txtNomeLivro

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

    txtNomeLivro.delete(0, END)  # limpa o que estava escrito na caixa de texto txtNomeAutor


# OPCAO 6
# def listeTodosLivros(conexao):

# OPCAO 7
# def liste_livros_ate_preco(conexao):

# OPCAO 8
# def liste_livros_faixa_preco(conexao):

# OPCAO 9
# def liste_livros_acima_preco(conexao):
'''

def programa():
    janela = Tk()

    # ---

    fonte = ("Verdana", "8")

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
    #btnBuscar["command"] = lambda: buscarLivro(conexao)
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

    global txtNomeAutor
    txtNomeAutor = Entry(painelNomeAutor)
    txtNomeAutor["width"] = 25
    txtNomeAutor["font"] = fonte
    txtNomeAutor.pack(side=LEFT)


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
    #bntInsert["command"] = lambda: cadastreLivro(conexao)
    bntInsert.pack(side=LEFT)

    bntExcluir = Button(painelDeBotoes, text="Remover", font=fonte, width=12)
    #bntExcluir["command"] = lambda: removaLivro(conexao)
    bntExcluir.pack(side=LEFT)




    #Listagens options

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
    #bntListar["command"] = lambda: listeTodosLivros(conexao)
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
    #bntListar["command"] = lambda: listeTodosLivros(conexao)
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
    #bntListar["command"] = lambda: listeTodosLivros(conexao)
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
    painelDeLista["padx"] = 50
    painelDeLista["pady"] = 15
    painelDeLista.pack()

    global listBox
    listBox=Listbox(painelDeLista)
    listBox["font"] = ("Verdana", "9", "italic")
    listBox.pack()

    # --- Painel dos botões

    painelDeBotoes = Frame(janela)
    painelDeBotoes["padx"] = 20
    painelDeBotoes["pady"] = 10
    painelDeBotoes.pack()

    bntListar = Button(painelDeBotoes, text="Listar Todos", font=fonte, width=24)
    #bntListar["command"] = lambda: listeTodosLivros(conexao)
    bntListar.pack(side=LEFT)

    # ---

    janela.mainloop()


programa()