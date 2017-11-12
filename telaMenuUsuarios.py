#coding: utf-8
from tkinter import *
import cadastrarUsuario as cadUsuario
import telaPrincipal as telaPrincipal
import funcoesUsuarios as funcUsuario

def construtorFormulario(niveldeAcesso):
    def novo_click():
        cadUsuario.construtorCadastoUsuario()

    MenuUsuarios = Tk()
    MenuUsuarios.title("Menu de Usuários")
    MenuUsuarios["bg"] = "#cbfbfe"
    MenuUsuarios.geometry("300x150+300+300")

    botaoEntrar = Button(MenuUsuarios, width = 16, text = "Novo Usuario", command = novo_click, background = "White",highlightcolor = "White")
    botaoEntrar.grid(row=1,column=2,sticky = W)