#coding: utf-8
import tkinter as tk
import telaCadastroPaciente as cadPaciente
import listaPacientes as listPacientes
import telaExcluirPaciente as excPaciente
import funcoesPacientes as funcPacientes
import telaMenuUsuarios as menuUsuarios
from tkinter import messagebox

dicionarioPacientes = {}

def construtorPrincipal(login,niveldeAcesso,parametro):
    def cadastrar_click():
        if niveldeAcesso != 0 and niveldeAcesso != 1 and niveldeAcesso != 2:
            messagebox.showinfo("Informação", "Voce não tem permissão para essa operação", icon='warning')
        else:
            cadPaciente.construtorFormulario(login,dicionarioPacientes,0)
    def editar_click():
        if niveldeAcesso != 0 and niveldeAcesso != 1:
            messagebox.showinfo("Informação", "Voce não tem permissão para essa operação", icon='warning')
        else:
            cadPaciente.construtorFormulario(login,dicionarioPacientes,1)
    def listar_click():
        listPacientes.construtorListaPacientes(login,dicionarioPacientes)
    def excluir_click():
        if niveldeAcesso != 0 and niveldeAcesso != 1:
            messagebox.showinfo("Informação", "Voce não tem permissão para essa operação", icon='warning')
        else:
            excPaciente.construtorDelPacientes(login,dicionarioPacientes)
    def logout_click():
        funcPacientes.CadastrasPacienteTxt(dicionarioPacientes)
        exit()
    def usuarios_click():
        if niveldeAcesso != 0 and niveldeAcesso != 1:
            messagebox.showinfo("Informação", "Voce não tem permissão para essa operação", icon='warning')
        else:
            menuUsuarios.construtorFormulario(niveldeAcesso)

    janelaPrincipal = tk.Toplevel()
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

    janelaPrincipal.mainloop()


