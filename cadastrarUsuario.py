# coding: utf-8
import tkinter as tk

def construtorCadastoUsuario():
    def button_click():
        loginUsuario = edLogin.get()
        senhaUsuario = edSenha.get()


    janelaCadUsuario = tk.Tk()
    janelaCadUsuario.title("Login")
    janelaCadUsuario["bg"] = "#cbfbfe"
    janelaCadUsuario.geometry("300x180+300+300")

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

    nivelAcesso = tk.IntVar()
    cbNivelAcesso1 = tk.Checkbutton(janelaCadUsuario, text="Super usuário", variable=nivelAcesso)
    cbNivelAcesso1.grid(row=3, column=1, sticky=tk.W)

    cbNivelAcesso2 = tk.Checkbutton(janelaCadUsuario, text="Gerente", variable=nivelAcesso)
    cbNivelAcesso2.grid(row=4, column=1, sticky=tk.W)

    cbNivelAcesso3 = tk.Checkbutton(janelaCadUsuario, text="Técnico", variable=nivelAcesso)
    cbNivelAcesso3.grid(row=5, column=1, sticky=tk.W)

    cbNivelAcesso4 = tk.Checkbutton(janelaCadUsuario, text="Estagiário", variable=nivelAcesso)
    cbNivelAcesso4.grid(row=6, column=1, sticky=tk.W)

    botaoEntrar = tk.Button(janelaCadUsuario, width=16, text="Cadastrar", command=button_click, background="White",
                         highlightcolor="White")
    botaoEntrar.grid(row=7, column=1, sticky=tk.W)

    janelaCadUsuario.mainloop()