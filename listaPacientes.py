from tkinter import *
from tkinter.ttk import *
import funcoesPacientes as funcPaciente

def construtorListaPacientes():
    def listarDicionario(dicionario):
        contDicionario = 0
        for cpf in dicionario.keys():
            contador = 0
            cpf1 = ""
            nome = ""
            rg = ""
            sexo = ""
            telefone = ""
            endereco = ""
            tipoSanguineo = ""
            informacoesGerais = ""
            for numero in dicionario[cpf]:
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

            tabelaPacientes.insert("", 'end', text="L"+str(contDicionario), values=(cpf,nome,rg,sexo,telefone,endereco,tipoSanguineo,informacoesGerais))
            cpf1 = ""
            nome = ""
            rg = ""
            sexo = ""
            telefone = ""
            endereco = ""
            tipoSanguineo = ""
            informacoesGerais = ""

        contDicionario += 1

    janelaListaPacientes = Tk()
    janelaListaPacientes.title("Lista de Pacientes")
    janelaListaPacientes["bg"] = "#cbfbfe"
    janelaListaPacientes.geometry("900x230+300+300")


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
    tabelaPacientes.grid(sticky = (N,S,W,E))
    tabelaPacientes.grid_rowconfigure(0, weight = 1)
    tabelaPacientes.grid_columnconfigure(0, weight = 1)

    tabela = funcPaciente.carregarPacientes()
    listarDicionario(tabela)

    janelaListaPacientes.mainloop()