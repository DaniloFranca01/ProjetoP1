import tkinter as tk
import funcoesPacientes as fpc
def construtorFormulario():
    def button_click():
        tuplaPaciente = (edCpf.get(),edNome.get(),edRg.get(),edTelefone.get(),edEndereco.get(),edTipoSanguineo.get(),edInformacoesGerais.get())
        fpc.CadastrasPaciente(tuplaPaciente)

    janeCadastroPaciente = tk.Tk()
    janeCadastroPaciente.title("Cadastro de paciente")
    janeCadastroPaciente["bg"] = "#cbfbfe"
    janeCadastroPaciente.geometry("450x200+300+300")

    lbNome = tk.Label(janeCadastroPaciente, text="Nome: ")
    lbNome.grid(row = 1)
    lbNome["bg"] = "#cbfbfe"
    edNome = tk.Entry(janeCadastroPaciente)
    edNome.grid(row = 1,column = 2)

    lbCpf = tk.Label(janeCadastroPaciente, text="CPF: ")
    lbCpf.grid(row = 2)
    lbCpf["bg"] = "#cbfbfe"
    edCpf = tk.Entry(janeCadastroPaciente)
    edCpf.grid(row = 2,column = 2)

    lbRg = tk.Label(janeCadastroPaciente, text="RG: ")
    lbRg.grid(row = 3)
    lbRg["bg"] = "#cbfbfe"
    edRg = tk.Entry(janeCadastroPaciente)
    edRg.grid(row = 3,column = 2)

    lbSexo = tk.Label(janeCadastroPaciente, text="Sexo: ")
    lbSexo.grid(row = 4)
    lbSexo["bg"] = "#cbfbfe"
    edSexo = tk.Entry(janeCadastroPaciente)
    edSexo.grid(row = 4,column = 2)

    lbTelefone = tk.Label(janeCadastroPaciente, text="Telefone: ")
    lbTelefone.grid(row = 5)
    lbTelefone["bg"] = "#cbfbfe"
    edTelefone = tk.Entry(janeCadastroPaciente)
    edTelefone.grid(row = 5,column = 2)


    lbEndereco = tk.Label(janeCadastroPaciente, text="Endereço: ")
    lbEndereco.grid(row = 6)
    lbEndereco["bg"] = "#cbfbfe"
    edEndereco = tk.Entry(janeCadastroPaciente)
    edEndereco.grid(row = 6,column = 2)

    lbTipoSanguineo = tk.Label(janeCadastroPaciente, text="Tipo Sanguineo: ")
    lbTipoSanguineo.grid(row = 7)
    lbTipoSanguineo["bg"] = "#cbfbfe"
    edTipoSanguineo = tk.Entry(janeCadastroPaciente)
    edTipoSanguineo.grid(row = 7,column = 2)

    lbInformacoesGerais = tk.Label(janeCadastroPaciente, text="Info. Gerais: ")
    lbInformacoesGerais.grid(row = 8)
    lbInformacoesGerais["bg"] = "#cbfbfe"
    edInformacoesGerais = tk.Entry(janeCadastroPaciente)
    edInformacoesGerais.grid(row = 8,column = 2)

    botaoCadastrar = tk.Button(janeCadastroPaciente, width = 16, text = "Cadastrar", command = button_click, background = "White",highlightcolor = "White")
    botaoCadastrar.grid(row=9,column = 2)


    janeCadastroPaciente.mainloop()
