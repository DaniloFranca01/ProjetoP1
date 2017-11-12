from bibliotecaFuncoes import criptografarInformacao,descriptografarInformacao
from tkinter import messagebox

def cadastrarUsuarioDicionario(login,tuplaUsuario,dicionario):
    '''
    Função que cadastra usuario em um dicionario
    recebe como parametro o login a tupla com informacoes e o dicionario de usuarios
    '''
    dicionario[login] = tuplaUsuario
    messagebox.showinfo("Informação", "Usuário cadastrado")
    return dicionario

def atualizarUsuarioDicionario(login,dicionario,valores):
    '''
    Função que atualiza o usuario em um dicionario
    recebe como parametro o login, o dicionario de usuarios e a tupla com informacoes e
    '''
    if login in dicionario.keys():
        del(dicionario[login])
        dicionario[login] = valores
        messagebox.showinfo("Informação", "Usuário Editado")
    return dicionario

def recebeUsuario(login,senha,dicionarioUsuarios):
    '''
    Função que recebe o usuario verificando se ele está cadastrado
    recebe como parametro o login,senha e o dicionario de usuarios
    '''
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
    '''
    Função que cadastra usuario em um arquivo TXT criptografado
    recebe como parametro o login, senha e o nivel de acesso
    '''
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
    '''
    Função que carrega de um TXT os usuarios para um dicionario
    '''
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


def cadastrarUsuariosTxt(dicionarioUsuarios):
    '''
    Função que cadastra um TXT os usuarios de um dicionario
    recebe como parametro um dicionario de usuarios
    '''
    arquivo = open("usuarios.txt", "r")
    conteudo = arquivo.readlines()

    login = ""
    senha = ""
    nivel = ""
    for valor in dicionarioUsuarios:
        login = criptografarInformacao(valor)
        senha = criptografarInformacao(dicionarioUsuarios[valor][0])
        nivel = criptografarInformacao(str(dicionarioUsuarios[valor][1]))
        conteudo.append(login + ";" + senha + ";" + nivel +"\n")

    arquivo = open("usuarios.txt", "w")
    arquivo.writelines(conteudo)
    arquivo.close()





