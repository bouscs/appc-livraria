from tkinter import *


# OPCAO 4
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

def programa():
    janela = Tk()

    # ---

    fonte = ("Verdana", "8")

    # ---

    painelDeOrientacao = Frame(janela)
    painelDeOrientacao["pady"] = 10
    painelDeOrientacao.pack()

    titulo = Label(painelDeOrientacao, text="Informe os dados :")
    titulo["font"] = ("Calibri", "9", "bold")
    titulo.pack()

    # ---

    painelDeBusca = Frame(janela)
    painelDeBusca["padx"] = 20
    painelDeBusca["pady"] = 5
    painelDeBusca.pack()

    lblIdUsuario = Label(painelDeBusca, text="Identificacao:", font=fonte, width=10)
    lblIdUsuario.pack(side=LEFT)

    txtIdUsuario = Entry(painelDeBusca)
    txtIdUsuario["width"] = 10
    txtIdUsuario["font"] = fonte
    txtIdUsuario.pack(side=LEFT)

    btnBuscar = Button(painelDeBusca, text="Buscar", font=fonte, width=10)
    #btnBuscar["command"] = buscarUsuario
    btnBuscar.pack(side=RIGHT)

    # ---

    painelDeNome = Frame(janela)
    painelDeNome["padx"] = 20
    painelDeNome["pady"] = 5
    painelDeNome.pack()

    lblnome = Label(painelDeNome, text="Nome:", font=fonte, width=10)
    lblnome.pack(side=LEFT)

    txtNome = Entry(painelDeNome)
    txtNome["width"] = 25
    txtNome["font"] = fonte
    txtNome.pack(side=LEFT)

    # ---

    painelDeTelefone = Frame(janela)
    painelDeTelefone["padx"] = 20
    painelDeTelefone["pady"] = 5
    painelDeTelefone.pack()

    lbltelefone = Label(painelDeTelefone, text="Telefone:", font=fonte, width=10)
    lbltelefone.pack(side=LEFT)

    txtTelefone = Entry(painelDeTelefone)
    txtTelefone["width"] = 25
    txtTelefone["font"] = fonte
    txtTelefone.pack(side=LEFT)

    # ---

    painelDeEmail = Frame(janela)
    painelDeEmail["padx"] = 20
    painelDeEmail["pady"] = 5
    painelDeEmail.pack()

    lblemail = Label(painelDeEmail, text="E-mail:", font=fonte, width=10)
    lblemail.pack(side=LEFT)

    txtEmail = Entry(painelDeEmail)
    txtEmail["width"] = 25
    txtEmail["font"] = fonte
    txtEmail.pack(side=LEFT)

    # ---

    painelDeUsuario = Frame(janela)
    painelDeUsuario["padx"] = 20
    painelDeUsuario["pady"] = 5
    painelDeUsuario.pack()

    lblusuario = Label(painelDeUsuario, text="Usuário:", font=fonte, width=10)
    lblusuario.pack(side=LEFT)

    txtUsuario = Entry(painelDeUsuario)
    txtUsuario["width"] = 25
    txtUsuario["font"] = fonte
    txtUsuario.pack(side=LEFT)

    # ---

    painelDeSenha = Frame(janela)
    painelDeSenha["padx"] = 20
    painelDeSenha["pady"] = 5
    painelDeSenha.pack()

    lblsenha = Label(painelDeSenha, text="Senha:", font=fonte, width=10)
    lblsenha.pack(side=LEFT)

    txtSenha = Entry(painelDeSenha)
    txtSenha["width"] = 25
    txtSenha["show"] = "*"
    txtSenha["font"] = fonte
    txtSenha.pack(side=LEFT)

    # ---

    painelDeBotoes = Frame(janela)
    painelDeBotoes["padx"] = 20
    painelDeBotoes["pady"] = 10
    painelDeBotoes.pack()

    bntInsert = Button(painelDeBotoes, text="Inserir", font=fonte, width=12)
    #bntInsert["command"] = inserirUsuario
    bntInsert.pack(side=LEFT)

    bntAlterar = Button(painelDeBotoes, text="Alterar", font=fonte, width=12)
    #bntAlterar["command"] = alterarUsuario
    bntAlterar.pack(side=LEFT)

    bntExcluir = Button(painelDeBotoes, text="Excluir", font=fonte, width=12)
    #bntExcluir["command"] = excluirUsuario
    bntExcluir.pack(side=LEFT)

    # ---

    painelDeMensagens = Frame(janela)
    painelDeMensagens["pady"] = 15
    painelDeMensagens.pack()

    lblmsg = Label(painelDeMensagens, text="Mensagem: ")
    lblmsg["font"] = ("Verdana", "9", "italic")
    lblmsg.pack()

    # ---

    janela.mainloop()


programa()