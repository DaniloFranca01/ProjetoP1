#coding: utf-8
from tkinter import *
import cadastrarUsuario as cadUsuario
import telaPrincipal as telaPrincipal
import funcoesUsuarios as funcUsuario

def logar_click():
    loginUsuario = edLogin.get()
    senhaUsuario = edSenha.get()
    niveldeAcesso = funcUsuario.recebeUsuario(loginUsuario,senhaUsuario,dicUsuarios)
    if niveldeAcesso != None:
        niveldeAcesso = int(niveldeAcesso)
        telaPrincipal.construtorPrincipal(loginUsuario,niveldeAcesso,0)

def novo_click():
    cadUsuario.construtorCadastoUsuario()


janelaLogin = Tk()
janelaLogin.title("Login")
janelaLogin["bg"] = "#cbfbfe"
janelaLogin.geometry("300x150+300+300")

imagem = PhotoImage(file="smmLogin.png")
lbImagem = Label(janelaLogin, image=imagem)
lbImagem.imagem = imagem
lbImagem["height"] = 70
lbImagem["width"] = 300
lbImagem.grid(row =0, columnspan = 300)

lbLogin = Label(janelaLogin, text="Login: ")
lbLogin.grid(row = 1)
lbLogin["bg"] = "#cbfbfe"
lbSenha = Label(janelaLogin, text="Senha: ")

lbSenha.grid(row = 2)
lbSenha["bg"] = "#cbfbfe"
edLogin = Entry(janelaLogin)
edLogin.grid(row = 1,column = 1,sticky = W)

edSenha = Entry(janelaLogin, show="*")
edSenha.grid(row = 2,column = 1, sticky = W)

botaoEntrar = Button(janelaLogin, width = 16, text = "Logar", command = logar_click, background = "White",highlightcolor = "White")
botaoEntrar.grid(row=3,column=1,sticky = W)

botaoEntrar = Button(janelaLogin, width = 16, text = "Novo Usuario", command = novo_click, background = "White",highlightcolor = "White")
botaoEntrar.grid(row=3,column=2,sticky = W)

dicUsuarios = funcUsuario.carregarUsuarios()

janelaLogin.mainloop()

