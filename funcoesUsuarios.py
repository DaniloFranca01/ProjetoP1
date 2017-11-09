from bibliotecaFuncoes import criptografarInformacao,descriptografarInformacao
from tkinter import messagebox

def recebeUsuario(login,senha,dicionarioUsuarios):
    for valor in dicionarioUsuarios:
        if login in dicionarioUsuarios.keys():
            senhaDicionario = dicionarioUsuarios[login][0]
            nivelAcesso = dicionarioUsuarios[login][1]
            if senha == senhaDicionario:
                return nivelAcesso
            else:
                messagebox.showinfo("Informação", "Senha incorreta", icon='warning')
                break
        else:
            messagebox.showinfo("Informação", "Usuario não cadastrado",icon='warning')
            break

def cadastrarUsuario(login,senha,nivel):
    arquivo = open("usuarios.txt", "r")

    conteudo = arquivo.readlines()

    loginCript = criptografarInformacao(login)
    senhaCript = criptografarInformacao(senha)
    nivelCript = criptografarInformacao(nivel)
    conteudo.append(loginCript+";"+senhaCript+";"+nivelCript+"\n")

    arquivo = open("usuarios.txt", "w")
    arquivo.writelines(conteudo)
    arquivo.close()
    messagebox.showinfo("Informação","Usuario cadastrado")

def carregarUsuarios():
    arquivo = open("usuarios.txt", "r")
    linha = arquivo.readline()
    loginCriptografado = ""
    senhaCriptografada = ""
    nivelAcessoCriptografado = ""
    dicionarioUsuarios = {}
    while linha != "":
        contador = 0
        for numero in linha:
            if numero != ";" and numero != "\n" and contador == 0:
                loginCriptografado = loginCriptografado + numero
            elif numero != ";" and numero != "\n" and contador == 1:
                senhaCriptografada = senhaCriptografada + numero
            elif numero != ";" and numero != "\n" and contador == 2:
                nivelAcessoCriptografado = nivelAcessoCriptografado + numero
            elif numero == ";":
                contador += 1
        login = descriptografarInformacao(loginCriptografado)
        senha = descriptografarInformacao(senhaCriptografada)
        nivelAcesso = descriptografarInformacao(nivelAcessoCriptografado)
        dicionarioUsuarios[login] = [senha, nivelAcesso]
        loginCriptografado = ""
        senhaCriptografada = ""
        nivelAcessoCriptografado = ""

        linha = arquivo.readline()
    arquivo.close()
    return dicionarioUsuarios





