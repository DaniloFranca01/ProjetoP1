from bibliotecaFuncoes import criptografarInformacao,descriptografarInformacao
from tkinter import messagebox

def recebeUsuario(login,senha):
        arquivo = open("usuarios.txt", "r")
        linha = arquivo.readline()
        flag = False
        loginCriptografado = ""
        while linha != "" and flag != True:
            for numero in linha:
                if numero != ";":
                    loginCriptografado = loginCriptografado + numero
                else:
                    if login != (loginCriptografado + descriptografarInformacao(loginCriptografado)):
                        return resultado
                        arquivo.write("")
                        arquivo.close()
                        flag = True

            linha = arquivo.readline()

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





