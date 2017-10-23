#coding: utf-8
from tkinter import *

def button_click():
    loginUsuario = edLogin.get()
    senhaUsuario = edSenha.get()

janelaLogin = Tk()
janelaLogin.title("Login")
janelaLogin["bg"] = "#cbfbfe"
janelaLogin.geometry("300x150+300+300")

imagem = PhotoImage(file="sme.png")
lbImagem = Label(janelaLogin, image=imagem)
lbImagem.imagem = imagem
lbImagem["height"] = 30
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

botaoEntrar = Button(janelaLogin, width = 16, text = "Logar", command = button_click, background = "White",highlightcolor = "White")
botaoEntrar.grid(row=3,column=1,sticky = W)

lbCadastro = Label(janelaLogin, text= "Não tem uma conta? Cadastre-se agora")
lbCadastro.grid(row = 5, column=1)
lbCadastro["bg"] = "#cbfbfe"



janelaLogin.mainloop()