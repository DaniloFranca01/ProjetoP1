import tkinter as tk
import tkinter.ttk as ttk
import telaPrincipal as telaPrincip
import funcoesUsuarios as funcUsuario
import bibliotecaFuncoes as bibliotecaFuncoes

def construtorFromulario(usuario,dicionario):
    '''
    Função que controi a interface de edicao de usuario
    recebe como parametro o dicionario de usuarios
    '''
    def pegarLogin():
        '''
        Função que pega o valor do login do combobox
        '''
        valorCombox = cbLogin.get()
        login = ""
        for letra in valorCombox:
            if letra != "-":
                login = login + letra
            elif letra == "-":
                break
        return login

    def editar_usuario():
        '''
        Função do evento click do botao editar que chama a funcao de edicao
        '''
        login = pegarLogin
        tuplaUsuario = (dicionario[login][1],dicionario[login][2])
        funcUsuario.atualizarUsuarioDicionario(login,dicionario,tuplaUsuario)
        bibliotecaFuncoes.logdeEventos(usuario, "Usuario editado" + "\n")


    janelaEditPermicaoUsuario = tk.Tk()
    janelaEditPermicaoUsuario.title("Editar permissão de Usuário")
    janelaEditPermicaoUsuario["bg"] = "#cbfbfe"
    janelaEditPermicaoUsuario.geometry("350x250+300+300")

    lbLogin = tk.Label(janelaEditPermicaoUsuario, text="Login: ")
    lbLogin.place(x = 0, y = 0)
    lbLogin["bg"] = "#cbfbfe"

    loginVar = tk.StringVar()
    cbLogin = ttk.Combobox(janelaEditPermicaoUsuario, textvariable=loginVar)
    cbLogin["state"] = "readonly"
    listaValores = []
    for valores in dicionario:
        listaValores.append(valores)
    cbLogin['values'] = (listaValores)
    cbLogin.place(x = 50, y = 0)

    listbNicelAcesso = tk.Listbox(janelaEditPermicaoUsuario)
    for item in ["Super usuário", "Gerente", "Técnico", "Estagiário"]:
        listbNicelAcesso.insert(tk.END, item)
    listbNicelAcesso.place(x= 50, y = 30)

    botaoEditar = tk.Button(janelaEditPermicaoUsuario, width=16, text="Editar", command=editar_usuario, background="White",highlightcolor="White")
    botaoEditar.place(x = 50, y =200)

    janelaEditPermicaoUsuario.mainloop()
    if dicionario != {} and telaPrincip.dicionarioUsuarios != {} :
        telaPrincip.dicionarioUsuarios = dicionario