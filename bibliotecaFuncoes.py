from datetime import datetime

def existeEm(carac, string):
    '''
    Função que procura um caracter em uma string, Função complemento da funcao tokenizar
    '''
    for elemento in string:
        if elemento == carac:
            return True
    return False


def tokenizar(frase, separadores):
    '''
    Função que tokeniza uma frase em uma lista
    '''
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


def incrementaDescriptografia(letraCodigoANSII):
    '''
    Função que axilia a criptografia de uma informacao
    recebe como parametro o codigo da tabela ANSII
    '''
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
    '''
    Função que criptografa uma informacao
    recebe como parametro a informacao a ser criptografada
    '''
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
    '''
    Função que descriptografa uma informacao
    recebe como parametro a informacao a ser descriptografada
    '''
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

def logdeEventos(usuario,evento):
    '''
    Função que salva em um TXT o log de toda atividade do usuario
    recebe como parametro o usuario e o evento
    '''
    arquivo = open("log.txt", "r")
    conteudo = arquivo.readlines()

    data = datetime.now()
    dia = str(data.day)
    mes = str(data.month)
    ano = str(data.year)
    hora = str(data.hour)
    minutos = str(data.minute)
    conteudo.append(dia+"/"+mes+"/"+ano+" - "+hora+":"+minutos + " " +usuario + " "+ evento )

    arquivo = open("log.txt", "w")
    arquivo.writelines(conteudo)
    arquivo.close()

