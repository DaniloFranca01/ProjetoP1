from bibliotecaFuncoes import criptografarInformacao,descriptografarInformacao

def recebeUsuario(login,senha):
        arquivo = open("usuarios.txt", "r")
        linha = arquivo.readline()
        flag = False
        loginCriptografado = ""
        while linha != "" and flag != True:
            for numero in linha:
                if numero != " ":
                    loginCriptografado = loginCriptografado + numero
                else:
                    if login != (loginCriptografado + descriptografarInformacao(loginCriptografado)):
                        return resultado
                        arquivo.write("")
                        arquivo.close()
                        CadastrasPaciente(cpf, nome, rg, telefone, endereco, tipoSanguineo, informacoesGerais)
                        flag = True

            linha = arquivo.readline()
