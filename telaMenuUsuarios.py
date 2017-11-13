from tkinter import *
import telaCadastrarUsuario as cadUsuario
import telaEditarPermicaoUsuario as editUsuario

def construtorFormulario(usuario,dicionario):
    '''
    Construtor do menu de usuarios recebe como parametro o nivel de acesso e o dicionario
    '''
    def novo_click():
        '''
        funcao do Evento do botao novo que chama o formulario de criacao de usuario
        '''
        cadUsuario.construtorCadastoUsuario(usuario,dicionario)
    def editar_click():
        '''
        funcao do Evento do botao editar que chama o formulario de edicao de usuario
        '''
        editUsuario.construtorFromulario(usuario,dicionario)

    menuUsuarios = Tk()
    menuUsuarios.title("Menu de Usuários")
    menuUsuarios["bg"] = "#cbfbfe"
    menuUsuarios.geometry("300x100+300+300")


    botaoNovoUsuario = Button(menuUsuarios, width = 16, text = "Novo Usuario", command = novo_click, background = "White",highlightcolor = "White")
    botaoNovoUsuario.grid(row=1,column=1,sticky = W)

    botaoEditarPermicao = Button(menuUsuarios, width=16, text="Editar permicao", command=editar_click, background="White",
                              highlightcolor="White")
    botaoEditarPermicao.grid(row=2, column=1, sticky=W)

    menuUsuarios.mainloop()
