from tkinter import *


def inserirUsuario():
    '''
    txtNome.get() recupera o que foi digitado na caixa de texto txtNome
    txtTelefone.get() recupera o que foi digitado na caixa de texto txtTelefone
    txtEmail.get() recupera o que foi digitado na caixa de texto txtEmail
    txtUsuario.get() recupera o que foi digitdo na caixa de texto txtUsuario
    txtSenha.get() recupera o que foi digitado na caixa de texto txtSenha

    AQUI A INSERCAO DE DADOS NO BD DEVE SER REALIZADA

    txtIdUsuario.delete(0,END) limpa o que estava escrito na caixa de texto txtIdUsuario
    txtNome.delete(0,END) limpa o que estava escrito na caixa de texto txtNome
    txtTelefone.delete(0,END) limpa o que estava escrito na caixa de texto txtTelefone
    txtEmail.delete(0,END) limpa o que estava escrito na caixa de texto txtEmail
    txtUsuario.delete(0,END) limpa o que estava escrito na caixa de texto txtUsuario
    txtSenha.delete(0,END) limpa o que estava escrito na caixa de texto txtSenha

    lblmsg["text"] = 'MENSAGEM DE SUCESSO OU INSUCESSO'
    '''


def alterarUsuario():
    '''
    txtNome.get() recupera o que foi digitado na caixa de texto txtNome
    txtTelefone.get() recupera o que foi digitado na caixa de texto txtTelefone
    txtEmail.get() recupera o que foi digitado na caixa de texto txtEmail
    txtUsuario.get() recupera o que foi digitdo na caixa de texto txtUsuario
    txtSenha.get() recupera o que foi digitado na caixa de texto txtSenha

    AQUI A ALTERACAO DE DADOS NO BD DEVE SER REALIZADA

    txtIdUsuario.delete(0,END) limpa o que estava escrito na caixa de texto txtIdUsuario
    txtNome.delete(0,END) limpa o que estava escrito na caixa de texto txtNome
    txtTelefone.delete(0,END) limpa o que estava escrito na caixa de texto txtTelefone
    txtEmail.delete(0,END) limpa o que estava escrito na caixa de texto txtEmail
    txtUsuario.delete(0,END) limpa o que estava escrito na caixa de texto txtUsuario
    txtSenha.delete(0,END) limpa o que estava escrito na caixa de texto txtSenha

    lblmsg["text"] = 'MENSAGEM DE SUCESSO OU INSUCESSO'
    '''


def excluirUsuario():
    '''
    txtIdUsuario.get() recupera o que foi digitdo na caixa de texto txtIdUsuario

    AQUI A EXCLUSAO DE DADOS DO BD DEVE SER REALIZADA

    txtIdUsuario.delete(0,END) limpa o que estava escrito na caixa de texto txtIdUsuario
    txtNome.delete(0,END) limpa o que estava escrito na caixa de texto txtNome
    txtTelefone.delete(0,END) limpa o que estava escrito na caixa de texto txtTelefone
    txtEmail.delete(0,END) limpa o que estava escrito na caixa de texto txtEmail
    txtUsuario.delete(0,END) limpa o que estava escrito na caixa de texto txtUsuario
    txtSenha.delete(0,END) limpa o que estava escrito na caixa de texto txtSenha

    lblmsg["text"] = 'MENSAGEM DE SUCESSO OU INSUCESSO'
    '''


def buscarUsuario():
    '''
    txtIdUsuario.get() recupera o que foi digitado na caixa de texto txtIdUsuario

    AQUI A CONSULTA DE DADOS DO BD DEVE SER REALIZADA, RECUPERANDO idusuario, nome, telefone, email, usuario e senha

    lblmsg["text"] = 'MENSAGEM DE SUCESSO OU INSUCESSO'

    txtIdUsuario.delete(0,END) limpa o que estava escrito na caixa de texto txtIdUsuario
    txtIdUsuario.insert(INSERT, idusuario) coloca idusuario na caixa de texto txtIdUsuario

    txtNome.delete(0,END) limpa o que estava escrito na caixa de texto txtNome
    txtNome.insert(INSERT, nome) coloca nome na caixa de texto txtNome

    txtTelefone.delete(0,END) limpa o que estava escrito na caixa de texto txtTelefone
    txtTelefone.insert(INSERT, telefone) coloca telefone na caixa de texto txtTelefone

    txtEmail.delete(0,END) limpa o que estava escrito na caixa de texto txtEmail
    txtEmail.insert(INSERT, email) coloca email na caixa de texto txtEmail

    txtUsuario.delete(0,END) limpa o que estava escrito na caixa de texto txtUsuario
    txtUsuario.insert(INSERT, usuario) coloca usuario na caixa de texto txtUsuario

    txtSenha.delete(0,END) limpa o que estava escrito na caixa de texto txtSenha
    txtSenha.insert(INSERT, senha) coloca senha na caixa de texto textsenha
    '''


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
    btnBuscar["command"] = buscarUsuario
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
    bntInsert["command"] = inserirUsuario
    bntInsert.pack(side=LEFT)

    bntAlterar = Button(painelDeBotoes, text="Alterar", font=fonte, width=12)
    bntAlterar["command"] = alterarUsuario
    bntAlterar.pack(side=LEFT)

    bntExcluir = Button(painelDeBotoes, text="Excluir", font=fonte, width=12)
    bntExcluir["command"] = excluirUsuario
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
