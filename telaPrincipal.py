import tkinter as tk
import telaCadastroPaciente as cadPaciente
import telaListarPacientes as listPacientes
import telaExcluirPaciente as excPaciente
import funcoesPacientes as funcPacientes
import telaMenuUsuarios as menuUsuarios
import funcoesUsuarios as funcUsuarios
from tkinter import messagebox

dicionarioPacientes = {}
dicionarioUsuarios = {}
def construtorPrincipal(login,niveldeAcesso,parametro):
    '''
    funcao construtora da tela principal recebe como parametro login,niveldeAcesso,parametro
    o parametro informa que é a primeira vez para poder carregar os pacientes e os usuarios
    '''

    def cadastrar_click():
        '''
        funcao do Evento do botao cadastrar que chama o formulario de cadastro de pacientes
        '''
        if niveldeAcesso != 0 and niveldeAcesso != 1 and niveldeAcesso != 2:
            messagebox.showinfo("Informação", "Voce não tem permissão para essa operação", icon='warning')
        else:
            cadPaciente.construtorFormulario(login,dicionarioPacientes,0)


    def editar_click():
        '''
        funcao do Evento do botao editar que chama o formulario de edicao de pacientes
        '''
        if niveldeAcesso != 0 and niveldeAcesso != 1:
            messagebox.showinfo("Informação", "Voce não tem permissão para essa operação", icon='warning')
        else:
            cadPaciente.construtorFormulario(login,dicionarioPacientes,1)


    def listar_click():
        '''
        funcao do Evento do botao listar que chama o formulario de listagem de pacientes
        '''
        listPacientes.construtorListaPacientes(login,dicionarioPacientes)


    def excluir_click():
        '''
        funcao do Evento do botao excluir que chama o formulario de exclusao de pacientes
        '''
        if niveldeAcesso != 0 and niveldeAcesso != 1:
            messagebox.showinfo("Informação", "Voce não tem permissão para essa operação", icon='warning')
        else:
            excPaciente.construtorDelPacientes(login,dicionarioPacientes)


    def logout_click():
        '''
        funcao do Evento do botao logout que chama salva as informacoes e fecha o programa
        '''
        funcPacientes.CadastrasPacienteTxt(dicionarioPacientes)
        funcUsuarios.cadastrarUsuariosTxt(dicionarioUsuarios)
        exit()


    def usuarios_click():
        '''
        funcao do Evento do botao de menu de usuario que chama o menu de usuario
        '''
        if niveldeAcesso != 0 and niveldeAcesso != 1:
            messagebox.showinfo("Informação", "Voce não tem permissão para essa operação", icon='warning')
        else:
            menuUsuarios.construtorFormulario(login,dicionarioUsuarios)


    janelaPrincipal = tk.Tk()

    janelaPrincipal.title("Medical Manager")
    janelaPrincipal["bg"] = "#cbfbfe"
    janelaPrincipal.geometry("732x360+300+300")

    logo = tk.PhotoImage(file="smm.png")
    lbImagem = tk.Label(janelaPrincipal, image=logo)
    lbImagem.logo = logo
    lbImagem["height"] = 311
    lbImagem["width"] = 658
    lbImagem.grid(row=1, columnspan=300)

    botaoCadastrar = tk.Button(janelaPrincipal, width = 16,height = 2, text = "Cadastrar Paciente", command = cadastrar_click, background = "White",highlightcolor = "White")
    botaoCadastrar.grid(row=2,column=1)

    botaoEditar = tk.Button(janelaPrincipal, width = 16,height = 2, text = "Editar Paciente", command = editar_click, background = "White",highlightcolor = "White")
    botaoEditar.grid(row=2,column=2)

    botaoExcluir = tk.Button(janelaPrincipal, width = 16,height = 2, text = "Excluir Paciente", command = excluir_click, background = "White",highlightcolor = "White")
    botaoExcluir.grid(row=2,column=3)

    botaoMostrar = tk.Button(janelaPrincipal, width = 16,height = 2, text = "Mostrar Paciente", command = listar_click, background = "White",highlightcolor = "White")
    botaoMostrar.grid(row=2,column=4)

    botaoUsuarios = tk.Button(janelaPrincipal, width=16, height=2, text="Menu de Usuarios", command=usuarios_click,
                            background="White", highlightcolor="White")
    botaoUsuarios.grid(row=2, column=5)

    botaoLogout = tk.Button(janelaPrincipal, width=16, height=2, text="Logout", command=logout_click,
                             background="White", highlightcolor="White")
    botaoLogout.grid(row=2, column=6)

    if parametro == 0:
        dicionarioPacientes = funcPacientes.carregarPacientes()
        dicionarioUsuarios = funcUsuarios.carregarUsuarios()

    janelaPrincipal.mainloop()


