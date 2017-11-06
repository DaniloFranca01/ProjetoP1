from bibliotecaFuncoes import criptografarInformacao,descriptografarInformacao

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
    arquivo = open("usuarios.txt", "w")
    loginCript = criptografarInformacao(login)
    senhaCript = criptografarInformacao(senha)
    nivelCript = criptografarInformacao(nivel)
    arquivo.write(loginCript+";"+senhaCript+";"+nivelCript)



