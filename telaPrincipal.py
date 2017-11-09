import tkinter as tk
import tkinter.filedialog
import telaCadastroPaciente as cadPaciente
import listaPacientes as listPacientes
import telaExcluirPaciente as excPaciente

def construtorPrincipal(niveldeAcesso):
    def cadastrar_click():
        cadPaciente.construtorFormulario()
    def editar_click():
        cadPaciente.construtorFormulario()
    def listar_click():
        listPacientes.construtorListaPacientes()
    def excluir_click():
        excPaciente.construtorDelFacientes()

    janelaPrincipal = tk.Tk()
    janelaPrincipal.title("Medical Manager")
    janelaPrincipal["bg"] = "#cbfbfe"
    janelaPrincipal.geometry("658x360+300+300")

    imagem = tk.PhotoImage(file="smm.png")
    lbImagem = tk.Label(janelaPrincipal, image=imagem)
    lbImagem.imagem = imagem
    lbImagem["height"] = 311
    lbImagem["width"] = 658
    lbImagem.grid(row=0, columnspan=300)

    botaoCadastrar = tk.Button(janelaPrincipal, width = 16,height = 2, text = "Cadastrar Paciente", command = cadastrar_click, background = "White",highlightcolor = "White")
    botaoCadastrar.grid(row=2,column=1)

    botaoEditar = tk.Button(janelaPrincipal, width = 16,height = 2, text = "Editar Paciente", command = editar_click, background = "White",highlightcolor = "White")
    botaoEditar.grid(row=2,column=2)

    botaoExcluir = tk.Button(janelaPrincipal, width = 16,height = 2, text = "Excluir Paciente", command = excluir_click, background = "White",highlightcolor = "White")
    botaoExcluir.grid(row=2,column=3)

    botaoMostrar = tk.Button(janelaPrincipal, width = 16,height = 2, text = "Mostrar Paciente", command = listar_click, background = "White",highlightcolor = "White")
    botaoMostrar.grid(row=2,column=4)

    botaoEditar.mainloop()


