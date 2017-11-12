import tkinter as tk
import tkinter.messagebox
import funcoesPacientes as fpc
import telaPrincipal as telaPrincipal
import tkinter.ttk as ttk
import bibliotecaFuncoes as bibliotecaFuncoes

def construtorDelPacientes(usuario,dicionario):
    '''
    Função que controi a interface de exclusao de pacientes recebe como parametro o usuario e o dicionario de pacientes
    '''
    def pegarCpf():
        '''
        Função que pega o cpf do combobox
        '''
        valorCombox = cbCpf.get()
        cpf = ""
        for letra in valorCombox:
            if letra != "-":
                cpf = cpf + letra
            elif letra == "-":
                break
        return cpf

    def button_click():
        '''
        Função do evento do botao que chama a funcao de exclusao
        '''
        resultado = tk.messagebox.askquestion("ATENÇÃO","Deseja excluir o paciente: ?",icon='warning')
        if resultado == "yes":
            cpf = pegarCpf()
            fpc.excluiPacienteDicionario(cpf,dicionario)
            bibliotecaFuncoes.logdeEventos(usuario, "Excluiu um paciente"+"\n")

    janelaExcluirPaciente = tk.Tk()
    janelaExcluirPaciente.title("Excluir paciente")
    janelaExcluirPaciente["bg"] = "#cbfbfe"
    janelaExcluirPaciente.geometry("250x100+300+300")

    lbCpf = tk.Label(janelaExcluirPaciente, text="CPF-Nome: ")
    lbCpf.grid(row=1, column=1)
    lbCpf["bg"] = "#cbfbfe"
    cpfVar = tk.StringVar()
    cbCpf = ttk.Combobox(janelaExcluirPaciente, textvariable=cpfVar)
    cbCpf["state"] = "readonly"
    listaValores = []
    for valores in dicionario:
        listaValores.append(valores + "-" + dicionario[valores][1])
    cbCpf['values'] = (listaValores)
    cbCpf.grid(row=1, column=2)

    botaoCadastrar = tk.Button(janelaExcluirPaciente, width = 16, text = "Excluir", command = button_click, background = "White",highlightcolor = "White")
    botaoCadastrar.grid(row=2,column = 2)

    janelaExcluirPaciente.mainloop()
    if dicionario != {} and telaPrincipal.dicionarioPacientes != {} :
        telaPrincipal.dicionarioPacientes = dicionario