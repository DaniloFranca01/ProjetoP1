# coding: utf-8
import tkinter as tk

def construtorCadastoUsuario():
    def button_click():
        loginUsuario = edLogin.get()
        senhaUsuario = edSenha.get()


    janelaLogin = tk.Tk()
    janelaLogin.title("Login")
    janelaLogin["bg"] = "#cbfbfe"
    janelaLogin.geometry("300x150+300+300")

    imagem = tk.PhotoImage(file="sme.png")
    lbImagem = tk.Label(janelaLogin, image=imagem)
    lbImagem.imagem = imagem
    lbImagem["height"] = 30
    lbImagem["width"] = 300
    lbImagem.grid(row=0, columnspan=300)

    lbLogin = tk.Label(janelaLogin, text="Login: ")
    lbLogin.grid(row=1)
    lbLogin["bg"] = "#cbfbfe"
    lbSenha = tk.Label(janelaLogin, text="Senha: ")

    lbSenha.grid(row=2)
    lbSenha["bg"] = "#cbfbfe"
    edLogin = tk.Entry(janelaLogin)
    edLogin.grid(row=1, column=1, sticky=tk.W)

    edSenha = tk.Entry(janelaLogin, show="*")
    edSenha.grid(row=2, column=1, sticky=tk.W)

    botaoEntrar = tk.Button(janelaLogin, width=16, text="Cadastrar", command=button_click, background="White",
                         highlightcolor="White")
    botaoEntrar.grid(row=3, column=1, sticky=tk.W)

    janelaLogin.mainloop()