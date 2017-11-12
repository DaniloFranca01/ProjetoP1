#coding: utf-8
from bibliotecaFuncoes import criptografarInformacao,descriptografarInformacao
from tkinter import messagebox
import telaCadastroPaciente as telaCadPaciente

def CadastrasPacienteTxt(dicionarioPacientes):
    '''
    Função que cadastra os pacientes do dicionario em um TXT criptografado
    recebe como parametro o dicionario de pacientes
    '''
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
    '''
    Função que cadastra um paciente no dicionario
    recebe como parametro o cpf, uma tupla de valores, e o dicionario de pacientes
    '''
    dicionarioPaciente[cpf] = tuplaPaciente
    messagebox.showinfo("Informação", "Paciente cadastrado")
    return dicionarioPaciente


def atualizarPacientesDicionario(cpf,dicionario,valores):
    '''
    Função que atualiza um paciente no dicionario
    recebe como parametro o cpf, o dicionario de pacientes e uma tupla de valores
    '''
    if cpf in dicionario.keys():
        del(dicionario[cpf])
        dicionario[cpf] = valores
        messagebox.showinfo("Informação", "Paciente Editado")
    return dicionario


def excluiPacienteDicionario(cpf,dicionario):
    '''
    Função que exclui um paciente do dicionario
    recebe como parametro o cpf e o dicionario de pacientes
    '''
    if cpf in dicionario.keys():
        del(dicionario[cpf])
        messagebox.showinfo("Informação", "Paciente Excluido")
    else:
        messagebox.showinfo("Informação", "Paciente Não encontrado")


def imprimePacientes(dicionario):
    '''
    Função que imprime em um TXT as informacoes de todos os pacientes sem criptografia
    recebe como parametro o dicionario de pacientes
    '''
    arqPacientes = open("impressaopacientes.txt", "r")
    conteudo = arqPacientes.readlines()
    for valor in dicionario:
        cpf = valor
        nome = dicionario[valor][0]
        rg = dicionario[valor][1]
        sexo = dicionario[valor][2]
        telefone = dicionario[valor][3]
        endereco = dicionario[valor][4]
        tipoSanguineo = dicionario[valor][5]
        informacoesGerais = dicionario[valor][6]
        conteudo.append("CPF:"+cpf + ";Nome: " + nome + ";RG: " + rg + ";Sexo: " + sexo + ";Telefone: " + telefone + ";Endereço: " + endereco + ";TipoSanguineo: " + tipoSanguineo + ";Informações: " + informacoesGerais + "\n")

    arqPacientes = open("impressaopacientes.txt", "w")
    arqPacientes.writelines(conteudo)
    arqPacientes.close()


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