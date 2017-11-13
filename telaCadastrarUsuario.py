import tkinter as tk
import funcoesUsuarios as userfunc
import bibliotecaFuncoes as bibliotecaFuncoes
import telaMenuUsuarios as menuUsuarios
import telaPrincipal as telaPrincip
dicionarioUsuarios = {}

def construtorCadastoUsuario(usuario,dicionario):
    '''
    Função que controi a interface de cadastro de usuario
    recebe como parametro o dicionario de usuarios
    '''
    def cadastrar_usuario():
        '''
        Função do evento click do botao cadastrar que chama a funcao de cadastro
        '''
        loginUsuario = edLogin.get()
        senhaUsuario = edSenha.get()
        tuplaAcesso = ()
        tuplaAcesso = listbNicelAcesso.curselection()[0]
        niveldeAcesso = int(tuplaAcesso)
        dicionarioUsuarios = userfunc.cadastrarUsuarioDicionario(loginUsuario,(senhaUsuario,niveldeAcesso),dicionario)
        bibliotecaFuncoes.logdeEventos(usuario, "Usuario cadastrado")

    janelaCadUsuario = tk.Tk()
    janelaCadUsuario.title("Cadastro de Usuário")
    janelaCadUsuario["bg"] = "#cbfbfe"
    janelaCadUsuario.geometry("300x200+300+300")

    lbLogin = tk.Label(janelaCadUsuario, text="Login: ")
    lbLogin.grid(row=1)
    lbLogin["bg"] = "#cbfbfe"
    lbSenha = tk.Label(janelaCadUsuario, text="Senha: ")

    lbSenha.grid(row=2)
    lbSenha["bg"] = "#cbfbfe"
    edLogin = tk.Entry(janelaCadUsuario)
    edLogin.grid(row=1, column=1, sticky=tk.W)

    edSenha = tk.Entry(janelaCadUsuario, show="*")
    edSenha.grid(row=2, column=1, sticky=tk.W)

    listbNicelAcesso = tk.Listbox(janelaCadUsuario)
    listbNicelAcesso.grid(row=3, column=1, sticky=tk.W)

    for item in ["Super usuário", "Gerente", "Técnico", "Estagiário"]:
        listbNicelAcesso.insert(tk.END, item)

    listbNicelAcesso.config(height=4)

    botaoCadastrar = tk.Button(janelaCadUsuario, width=16, text="Cadastrar", command=cadastrar_usuario, background="White",
                         highlightcolor="White")

    botaoCadastrar.grid(row=7, column=1, sticky=tk.W)

    janelaCadUsuario.mainloop()
    if dicionario != {} and telaPrincip.dicionarioUsuarios != {} :
        telaPrincip.dicionarioUsuarios = dicionario