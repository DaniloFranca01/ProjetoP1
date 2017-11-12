#coding: utf-8
from bibliotecaFuncoes import criptografarInformacao,descriptografarInformacao
from tkinter import messagebox
import telaCadastroPaciente as telaCadPaciente

def CadastrasPacienteTxt(dicionarioPacientes):
    arqPacientes = open("pacientes.txt", "r")
    conteudo = arqPacientes.readlines()

    cpf = ""
    nome = ""
    rg = ""
    sexo = ""
    telefone = ""
    endereco = ""
    tipoSanguineo = ""
    informacoesGerais = ""
    for valor in dicionarioPacientes:
        cpf = criptografarInformacao(valor)
        nome = criptografarInformacao(dicionarioPacientes[valor][0])
        rg = criptografarInformacao(dicionarioPacientes[valor][1])
        sexo = criptografarInformacao(dicionarioPacientes[valor][2])
        telefone = criptografarInformacao(dicionarioPacientes[valor][3])
        endereco = criptografarInformacao(dicionarioPacientes[valor][4])
        tipoSanguineo = criptografarInformacao(dicionarioPacientes[valor][5])
        informacoesGerais = criptografarInformacao(dicionarioPacientes[valor][6])

    conteudo.append(cpf + ";" + nome + ";" + rg + ";" + sexo + ";" + telefone + ";" + endereco + ";" + tipoSanguineo + ";" + informacoesGerais+"\n")
    arqPacientes = open("pacientes.txt", "w")
    arqPacientes.writelines(conteudo)
    arqPacientes.close()


def CadastrarPacienteDicionario(cpf,tuplaPaciente,dicionarioPaciente):
    dicionarioPaciente[cpf] = tuplaPaciente
    messagebox.showinfo("Informação", "Paciente cadastrado")
    return dicionarioPaciente

def atualizarPacientesDicionario(cpf,dicionario,valores):
    if cpf in dicionario.keys():
        del(dicionario[cpf])
        dicionario[cpf] = valores
        messagebox.showinfo("Informação", "Paciente Editado")
    return dicionario

def excluiPacienteDicionario(cpf,dicionario):
    if cpf in dicionario.keys():
        del(dicionario[cpf])
        messagebox.showinfo("Informação", "Paciente Excluido")
    else:
        messagebox.showinfo("Informação", "Paciente Não encontrado")

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
                    dicionario = {}
                    dicionario[cpf] = (nome, rg, sexo, telefone, endereco, tipoSanguineo, informacoesGerais)
                    CadastrasPacienteTxt(dicionario)
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
    '''
    Função que carrega os pacientes do TXT para o dicionario de pacientes

    '''
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
        dicionarioPacientes[cpf] = (nome, rg, sexo, telefone, endereco, tipoSanguineo, informacoesGerais)
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