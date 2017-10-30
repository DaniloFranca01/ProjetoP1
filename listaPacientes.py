from tkinter import *
from tkinter.ttk import *

def construtorListaPacientes():
    janelaListaPacientes = Tk()
    janelaListaPacientes.title("Lista de Pacientes")
    janelaListaPacientes["bg"] = "#cbfbfe"
    janelaListaPacientes.geometry("1005x230+300+300")

    tabelaPacientes = Treeview()
    tabelaPacientes['columns'] = ('cpf', 'nome', 'rg','sexo','telefone','endereco','tipoSanguineo','informacoes')
    tabelaPacientes.heading("#0", text='Nunemro', anchor='w')
    tabelaPacientes.column("#0", anchor="w")
    tabelaPacientes.heading('cpf', text='CPF')
    tabelaPacientes.column('cpf', anchor='center', width=100)
    tabelaPacientes.heading('nome', text='Nome')
    tabelaPacientes.column('nome', anchor='center', width=100)
    tabelaPacientes.heading('rg', text='RG')
    tabelaPacientes.column('rg', anchor='center', width=100)
    tabelaPacientes.heading('sexo', text='Sexo')
    tabelaPacientes.column('sexo', anchor='center', width=100)
    tabelaPacientes.heading('telefone', text='Telefone')
    tabelaPacientes.column('telefone', anchor='center', width=100)
    tabelaPacientes.heading('endereco', text='Endereço')
    tabelaPacientes.column('endereco', anchor='center', width=100)
    tabelaPacientes.heading('tipoSanguineo', text='Tp.Sanguineo')
    tabelaPacientes.column('tipoSanguineo', anchor='center', width=100)
    tabelaPacientes.heading('informacoes', text='Info')
    tabelaPacientes.column('informacoes', anchor='center', width=100)

    tabelaPacientes.grid(sticky = (N,S,W,E))
    tabelaPacientes.grid_rowconfigure(0, weight = 1)
    tabelaPacientes.grid_columnconfigure(0, weight = 1)

    janelaListaPacientes.mainloop()

construtorListaPacientes()