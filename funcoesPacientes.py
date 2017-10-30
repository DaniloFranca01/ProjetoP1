#coding: utf-8
from bibliotecaFuncoes import criptografarInformacao,descriptografarInformacao


def CadastrasPaciente(tuplaPaciente):
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

    arqPacientes = open("pacientes.txt", "w")
    arqPacientes.write(cpf+" "+nome+" "+rg+" "+sexo+" "+telefone+" "+endereco+" "+tipoSanguineo+" "+informacoesGerais)
    arqPacientes.flush()
    arqPacientes.close()


def atualizarPaciente(cpf,nome,rg,telefone,endereco,tipoSanguineo,informacoesGerais):
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
                    CadastrasPaciente(cpf, nome, rg, telefone, endereco, tipoSanguineo, informacoesGerais)
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


'''CadastrasPaciente(("53409360","Danilo","8637637","3010","R5","O+","deprecao"))
resultado2 = atualizarPaciente("53409360","kkkkk","99999","5000","R1","A+","Curado")
resultado3 = excluirPaciente("53409360")'''