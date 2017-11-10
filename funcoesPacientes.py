#coding: utf-8
from bibliotecaFuncoes import criptografarInformacao,descriptografarInformacao
from tkinter import messagebox

def CadastrasPaciente(tuplaPaciente):
    arqPacientes = open("usuarios.txt", "r")
    conteudo = arqPacientes.readlines()

    cpf = ""
    nome = ""
    rg = ""
    sexo = ""
    telefone = ""
    endereco = ""
    tipoSanguineo = ""
    informacoesGerais = ""
    contador = 0
    for valor in tuplaPaciente:
        if contador == 0:
            cpf = criptografarInformacao(valor)
        elif contador == 1:
            nome = criptografarInformacao(valor)
        elif contador == 2:
            rg = criptografarInformacao(valor)
        elif contador == 3:
            sexo = criptografarInformacao(valor)
        elif contador == 4:
            telefone = criptografarInformacao(valor)
        elif contador == 5:
            endereco = criptografarInformacao(valor)
        elif contador == 6:
            tipoSanguineo = criptografarInformacao(valor)
        elif contador == 7:
            informacoesGerais = criptografarInformacao(valor)
        contador+=1

    conteudo.append(cpf + ";" + nome + ";" + rg + ";" + sexo + ";" + telefone + ";" + endereco + ";" + tipoSanguineo + ";" + informacoesGerais+"\n")
    arqPacientes = open("usuarios.txt", "w")
    arqPacientes.writelines(conteudo)
    arqPacientes.close()
    messagebox.showinfo("Informação", "Paciente cadastrado")


def atualizarPaciente(cpf,nome,rg,sexo,telefone,endereco,tipoSanguineo,informacoesGerais):
    arquivo = open("pacientes.txt", "r")
    linha = arquivo.readline()
    flag = False
    letraCriptografada = ""
    while linha != "" and flag != True:
        for numero in linha:
            if numero != " ":
               letraCriptografada = letraCriptografada+numero
            else:
                if cpf == (letraCriptografada + descriptografarInformacao(letraCriptografada) ):
                    arquivo.write("")
                    arquivo.close()
                    CadastrasPaciente(cpf, nome, rg, sexo, telefone, endereco, tipoSanguineo, informacoesGerais)
                    flag = True

        linha = arquivo.readline()

        if flag == True:
            resultado = "Paciente editado com sucesso!"
        else:
            resultado = "Paciente provavelmente não cadastrado!"
    return resultado


def excluirPaciente(cpf):
    arquivo = open("pacientes.txt", "r")
    linha = arquivo.readline()
    flag = False
    while linha != "" and flag != True:
        letraCriptografada = ""
        for numero in linha:
            if numero != " ":
                letraCriptografada = letraCriptografada + numero
            else:
                if cpf == (letraCriptografada + descriptografarInformacao(letraCriptografada) ):
                    arquivo.write("")
                    arquivo.close()
                    flag = True

        linha = arquivo.readline()

        if flag == True:
            resultado = "Paciente removido com sucesso!"
        else:
            resultado = "Paciente provavelmente não cadastrado!"
    return resultado

def carregarPacientes():
    arquivo = open("pacientes.txt", "r")
    dicionarioPacientes={}
    linha = arquivo.readline()
    cpfCriptografado = ""
    nomeCriptografado = ""
    rgCriptografado = ""
    sexoCriptografado = ""
    telefoneCriptografado = ""
    enderecoCriptografado = ""
    tipoSanguineoCriptografado = ""
    informacoesGeraisCriptografado = ""
    while linha != "":
        contador = 0
        for numero in linha:
            if numero != ";" and numero != "\n" and contador == 0:
                cpfCriptografado = cpfCriptografado + numero
            elif numero != ";" and numero != "\n" and contador == 1:
                nomeCriptografado = nomeCriptografado + numero
            elif numero != ";" and numero != "\n" and contador == 2:
                rgCriptografado = rgCriptografado + numero
            elif numero != ";" and numero != "\n" and contador == 3:
                sexoCriptografado = sexoCriptografado + numero
            elif numero != ";" and numero != "\n" and contador == 4:
                telefoneCriptografado = telefoneCriptografado + numero
            elif numero != ";" and numero != "\n" and contador == 5:
                enderecoCriptografado = enderecoCriptografado + numero
            elif numero != ";" and numero != "\n" and contador == 6:
                tipoSanguineoCriptografado = tipoSanguineoCriptografado + numero
            elif numero != ";" and numero != "\n" and contador == 7:
                informacoesGeraisCriptografado = informacoesGeraisCriptografado + numero
            elif numero == ";":
                contador += 1

        cpf = descriptografarInformacao(cpfCriptografado)
        nome = descriptografarInformacao(nomeCriptografado)
        rg = descriptografarInformacao(rgCriptografado)
        sexo = descriptografarInformacao(sexoCriptografado)
        telefone = descriptografarInformacao(telefoneCriptografado)
        endereco = descriptografarInformacao(enderecoCriptografado)
        tipoSanguineo = descriptografarInformacao(tipoSanguineoCriptografado)
        informacoesGerais = descriptografarInformacao(informacoesGeraisCriptografado)
        dicionarioPacientes[cpf] = [nome, rg, sexo, telefone, endereco, tipoSanguineo, informacoesGerais]
        cpfCriptografado = ""
        nomeCriptografado = ""
        rgCriptografado = ""
        sexoCriptografado = ""
        telefoneCriptografado = ""
        enderecoCriptografado = ""
        tipoSanguineoCriptografado = ""
        informacoesGeraisCriptografado = ""

        linha = arquivo.readline()
    arquivo.close()
    return dicionarioPacientes


'''CadastrasPaciente(("53409360","Danilo","8637637","3010","R5","O+","deprecao"))
resultado2 = atualizarPaciente("53409360","kkkkk","99999","5000","R1","A+","Curado")
resultado3 = excluirPaciente("53409360")'''