from tkinter import *

def programa():
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

    txtIdAutor = Entry(painelDeBusca)
    txtIdAutor["width"] = 10
    txtIdAutor["font"] = fonte
    txtIdAutor.pack(side=LEFT)

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
    #bntInsert["command"] = cadastreAutor
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
