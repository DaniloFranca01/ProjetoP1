import tkinter as tk
import funcoesPacientes as fpc
import telaPrincipal as telaPrincipal
import tkinter.ttk as ttk

def construtorFormulario(dicionario,parametro):
    def pegarCpf():
        valorCombox = cbCpf.get()
        cpf = ""
        for letra in valorCombox:
            if letra != "-":
                cpf = cpf + letra
            elif letra == "-":
                break
        return cpf

    def limparEdits():
        if parametro == 0:
            edCpf.delete(0,tk.END)
        edNome.delete(0, tk.END)
        edRg.delete(0, tk.END)
        edSexo.delete(0, tk.END)
        edTelefone.delete(0, tk.END)
        edEndereco.delete(0, tk.END)
        edTipoSanguineo.delete(0, tk.END)
        edInformacoesGerais.delete(0, tk.END)

    def cadastrar_click():
        tuplaPaciente = (edCpf.get(),edNome.get(),edRg.get(),edSexo.get(),edTelefone.get(),edEndereco.get(),edTipoSanguineo.get(),edInformacoesGerais.get())
        fpc.CadastrarPacienteDicionario(edCpf.get(),tuplaPaciente,dicionario)
        limparEdits()

    def editar_click():
        tuplaPaciente = (edNome.get(), edRg.get(), edSexo.get(), edTelefone.get(), edEndereco.get(), edTipoSanguineo.get(),edInformacoesGerais.get())
        cpf = pegarCpf()
        fpc.atualizarPacientesDicionario(cpf,dicionario,tuplaPaciente)
        limparEdits()

    def selecionaPaciente(parametro):
        cpf = pegarCpf()
        if cpf in dicionario:
            limparEdits()
            edNome.insert(0,dicionario[cpf][1])
            edRg.insert(0, dicionario[cpf][2])
            edSexo.insert(0, dicionario[cpf][3])
            edTelefone.insert(0, dicionario[cpf][4])
            edEndereco.insert(0, dicionario[cpf][5])
            edTipoSanguineo.insert(0, dicionario[cpf][6])
            edInformacoesGerais.insert(0, dicionario[cpf][7])


    janeCadastroPaciente = tk.Tk()
    if parametro == 0:
        janeCadastroPaciente.title("Cadastro de paciente")
    else:
        janeCadastroPaciente.title("Editar paciente")
    janeCadastroPaciente["bg"] = "#cbfbfe"
    janeCadastroPaciente.geometry("300x200+300+300")

    if parametro == 0:
        lbCpf = tk.Label(janeCadastroPaciente, text="CPF: ")
        lbCpf.grid(row=1, column=1)
        lbCpf["bg"] = "#cbfbfe"
        edCpf = tk.Entry(janeCadastroPaciente)
        edCpf.grid(row = 1,column = 2)
    else:
        lbCpf = tk.Label(janeCadastroPaciente, text="CPF-Nome: ")
        lbCpf.grid(row=1, column=1)
        lbCpf["bg"] = "#cbfbfe"
        cpfVar = tk.StringVar()
        cbCpf = ttk.Combobox(janeCadastroPaciente, textvariable=cpfVar)
        cbCpf["state"] = "readonly"
        listaValores = []
        for valores in dicionario:
            listaValores.append(valores+"-"+dicionario[valores][1])
        cbCpf['values'] = (listaValores)
        cbCpf.grid(row=1, column=2)
        cbCpf.bind("<<ComboboxSelected>>", selecionaPaciente)

    lbNome = tk.Label(janeCadastroPaciente, text="Nome: ")
    lbNome.grid(row = 2,column = 1)
    lbNome["bg"] = "#cbfbfe"
    edNome = tk.Entry(janeCadastroPaciente)
    edNome.grid(row = 2,column = 2)

    lbRg = tk.Label(janeCadastroPaciente, text="RG: ")
    lbRg.grid(row = 3, column = 1)
    lbRg["bg"] = "#cbfbfe"
    edRg = tk.Entry(janeCadastroPaciente)
    edRg.grid(row = 3,column = 2)

    lbSexo = tk.Label(janeCadastroPaciente, text="Sexo: ")
    lbSexo.grid(row = 4, column = 1)
    lbSexo["bg"] = "#cbfbfe"
    edSexo = tk.Entry(janeCadastroPaciente)
    edSexo.grid(row = 4,column = 2)

    lbTelefone = tk.Label(janeCadastroPaciente, text="Telefone: ")
    lbTelefone.grid(row = 5,column = 1)
    lbTelefone["bg"] = "#cbfbfe"
    edTelefone = tk.Entry(janeCadastroPaciente)
    edTelefone.grid(row = 5,column = 2)


    lbEndereco = tk.Label(janeCadastroPaciente, text="Endereço: ")
    lbEndereco.grid(row = 6,column = 1)
    lbEndereco["bg"] = "#cbfbfe"
    edEndereco = tk.Entry(janeCadastroPaciente)
    edEndereco.grid(row = 6,column = 2)

    lbTipoSanguineo = tk.Label(janeCadastroPaciente, text="Tipo Sanguineo: ")
    lbTipoSanguineo.grid(row = 7,column = 1)
    lbTipoSanguineo["bg"] = "#cbfbfe"
    edTipoSanguineo = tk.Entry(janeCadastroPaciente)
    edTipoSanguineo.grid(row = 7,column = 2)

    lbInformacoesGerais = tk.Label(janeCadastroPaciente, text="Info. Gerais: ")
    lbInformacoesGerais.grid(row = 8,column = 1)
    lbInformacoesGerais["bg"] = "#cbfbfe"
    edInformacoesGerais = tk.Entry(janeCadastroPaciente)
    edInformacoesGerais.grid(row = 8,column = 2)

    if parametro == 0:
        botaoCadastrar = tk.Button(janeCadastroPaciente, width = 16, text = "Cadastrar", command = cadastrar_click, background = "White",highlightcolor = "White")
        botaoCadastrar.grid(row=9,column = 2)
    else:
        botaoEditar = tk.Button(janeCadastroPaciente, width=16, text="Editar", command=editar_click, background="White", highlightcolor="White")
        botaoEditar.grid(row=9, column=2)


    janeCadastroPaciente.mainloop()
    if dicionario != {} and telaPrincipal.dicionarioPacientes != {} :
        telaPrincipal.dicionarioPacientes = dicionario

