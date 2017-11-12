import tkinter as tk
from tkinter.ttk import *
import funcoesPacientes as funcPaciente
import bibliotecaFuncoes as bibliotecaFuncoes


def construtorListaPacientes(usuario,dicionarioPacientes):
    '''
    Função que constroi a tela de listar pacientes recebe de parametro o usuario e o dicionario de pacientes
    '''
    def listarDicionario(dicionarioPacientes):
        '''
        Função que alimenta a tabela com os pacientes, recebe de parametro o dicionario de pacientes
        '''
        contDicionario = 0
        for cpf in dicionarioPacientes.keys():
            contador = 0
            cpf1 = ""
            nome = ""
            rg = ""
            sexo = ""
            telefone = ""
            endereco = ""
            tipoSanguineo = ""
            informacoesGerais = ""
            for numero in dicionarioPacientes[cpf]:
                cpf1 = cpf
                if contador == 0:
                    nome = nome + numero
                elif contador == 1:
                    rg = rg + numero
                elif contador == 2:
                    sexo = sexo + numero
                elif contador == 3:
                    telefone = telefone + numero
                elif contador == 4:
                    endereco = endereco + numero
                elif contador == 5:
                    tipoSanguineo = tipoSanguineo + numero
                elif contador == 6:
                    informacoesGerais = informacoesGerais + numero
                contador += 1

            tabelaPacientes.insert("", 'end', text=cpf1, values=(cpf,nome,rg,sexo,telefone,endereco,tipoSanguineo,informacoesGerais))
            cpf1 = ""
            nome = ""
            rg = ""
            sexo = ""
            telefone = ""
            endereco = ""
            tipoSanguineo = ""
            informacoesGerais = ""

        contDicionario += 1

    def imprimir_click():
        '''
        Função do evento imprimir que chama a funcao de imprecao de pacientes em TXT sem criptografia
        '''
        funcPaciente.imprimePacientes(dicionarioPacientes)

    def pesquisaPaciente(item=''):
        '''
        Função do evento do botao pesquisar que procura e marca no treeview o elemento encontrado
        '''
        children = tabelaPacientes.get_children(item)
        for child in children:
            text = tabelaPacientes.item(child, 'text')
            if text == (edPesquisa.get()):
                tabelaPacientes.selection_set(child)
                return True
            else:
                res = pesquisaPaciente(child)
                if res:
                    return True

    janelaListaPacientes = tk.Tk()
    janelaListaPacientes.title("Lista de Pacientes")
    janelaListaPacientes["bg"] = "#cbfbfe"
    janelaListaPacientes.geometry("900x300+300+300")

    lbPesquisa = tk.Label(janelaListaPacientes, text = "CPF:")
    lbPesquisa.place(x=10, y=5)
    lbPesquisa["bg"] = "#cbfbfe"

    edPesquisa = tk.Entry(janelaListaPacientes)
    edPesquisa.place(x=50, y=5)

    botaoPesquisar = tk.Button(janelaListaPacientes, width=16, text="Pesquisar", command=pesquisaPaciente,background="White", highlightcolor="White")
    botaoPesquisar.place(x = 180, y = 3)

    tabelaPacientes = Treeview(janelaListaPacientes)
    tabelaPacientes['columns'] = ('cpf', 'nome', 'rg','sexo','telefone','endereco','tipoSanguineo','informacoes')
    tabelaPacientes['show'] = 'headings'
    tabelaPacientes.heading('#0', text='CPF',  anchor='center')
    tabelaPacientes.column('#0', width=100, anchor="center")
    tabelaPacientes.heading('#1', text='CPF',  anchor='center')
    tabelaPacientes.column('#1', width=100, anchor="center")
    tabelaPacientes.heading('#2', text='Nome')
    tabelaPacientes.column('#2', anchor='center', width=100)
    tabelaPacientes.heading('#3', text='RG')
    tabelaPacientes.column('#3', anchor='center', width=100)
    tabelaPacientes.heading('#4', text='Sexo')
    tabelaPacientes.column('#4', anchor='center', width=100)
    tabelaPacientes.heading('#5', text='Telefone')
    tabelaPacientes.column('#5', anchor='center', width=100)
    tabelaPacientes.heading('#6', text='Endereço')
    tabelaPacientes.column('#6', anchor='center', width=100)
    tabelaPacientes.heading('#7', text='Tp.Sanguineo')
    tabelaPacientes.column('#7', anchor='center', width=100)
    tabelaPacientes.heading('#8', text='Info')
    tabelaPacientes.column('#8', anchor='center', width=100)
    tabelaPacientes.place(x = 10, y = 30)

    botaoImprimirPacientes = tk.Button(janelaListaPacientes, width=16, text="Imprimir", command=imprimir_click, background="White", highlightcolor="White")
    botaoImprimirPacientes.place(x = 750, y = 260)

    listarDicionario(dicionarioPacientes)
    bibliotecaFuncoes.logdeEventos(usuario, "Listou os pacientes"+"\n")
    janelaListaPacientes.mainloop()