def existeEm(carac, string):
    for elemento in string:
        if elemento == carac:
            return True
    return False


def tokenizar(frase, separadores):
    lista = []
    palavra = ""
    for letra in frase:
        for elemento in separadores:
            if elemento != letra:
                palavra = palavra + letra
            else:
                if palavra != "":
                    lista.append(palavra)
                    palavra = ""
    if palavra != "":
        lista.append(palavra)

    return lista

def criptografarLogin(login,senha):
    loginCriptografado = ""
    senhaCriptogrfada = ""
    primeiraVez = True
    for letra in login:
        if primeiraVez:
            loginCriptografado = str(ord(letra)+37)
            primeiraVez = False
        else:
            loginCriptografado = loginCriptografado + " " + str(ord(letra) + 37)

    primeiraVez = True
    for letra in senha:
        if primeiraVez:
            senhaCriptogrfada = str(ord(letra)+37)
            primeiraVez = False
        else:
            senhaCriptogrfada = senhaCriptogrfada + " " + str(ord(letra) + 37)

    arqUsuarios = open("usuarios.txt", "w")
    arqUsuarios.write(loginCriptografado+";"+senhaCriptogrfada)

def incrementaDescriptografia(letraCodigoANSII):
    numeroCriptografado = int(letraCodigoANSII) - 37
    letraCriptografada = chr(numeroCriptografado)
    return letraCriptografada

def descriptografarLogin():
    arquivo = open("usuarios.txt", "r")
    linha = arquivo.readline()
    login = ""
    senha = ""
    tuplaLogin = ()
    letraCriptografada = ""
    while linha != "":
        flag = 0
        for numero in linha:
            if numero != " " and numero != ";":
               letraCriptografada = letraCriptografada+numero
            elif numero == ";":
                login = login + incrementaDescriptografia(letraCriptografada)
                flag = 1
            else:
                if flag == 0:
                    login = login +incrementaDescriptografia(letraCriptografada)
                if flag == 1 and numero != ";":
                    senha = senha+incrementaDescriptografia(letraCriptografada)
                letraCriptografada = ""

        linha = arquivo.readline()

    tuplaLogin = login+" "+senha

    return tuplaLogin


def criptografarInformacao(informacao):
    informacaoCriptografada = ""
    primeiraVez = True
    for letra in informacao:
        if primeiraVez:
            informacaoCriptografada = str(ord(letra)+37)
            primeiraVez = False
        else:
            informacaoCriptografada = informacaoCriptografada + " " + str(ord(letra) + 37)

    return informacaoCriptografada

def descriptografarInformacao(informacao):
    informacaoDescriptografada = ""
    partedaInformacao = ""
    tamanhoInformacao = len(informacao)
    contador = 0
    while contador <= tamanhoInformacao:
        if (contador == tamanhoInformacao):
            informacaoDescriptografada = informacaoDescriptografada+incrementaDescriptografia(partedaInformacao)
            partedaInformacao = ""
        elif informacao[contador] == " ":
            informacaoDescriptografada = informacaoDescriptografada+incrementaDescriptografia(partedaInformacao)
            partedaInformacao = ""
        elif informacao[contador] != " ":
            partedaInformacao = partedaInformacao+informacao[contador]
        contador += 1
    return informacaoDescriptografada


#criptografarLogin("Danilo","123")
#descriptografarLogin()