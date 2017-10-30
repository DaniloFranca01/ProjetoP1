import tkinter as tk
import tkinter.filedialog
import telaCadastroPaciente as cadPaciente
def construtorPrincipal():
    def cadastrar_click():
        cadPaciente.construtorFormulario()
    def editar_click():
        tkinter.FileDialog.telaCadastroPaciente

    janelaPrincipal = tk.Tk()
    janelaPrincipal.title("Medical Manager")
    janelaPrincipal["bg"] = "#cbfbfe"
    janelaPrincipal.geometry("658x360+300+300")
    #bordaDireita  = tk.Label(janelaPrincipal, background = "Blue",height = 400).grid(row = 0,column=0)
    #bordaEsquerda  = tk.Label(janelaPrincipal, background = "Blue",height = 400).grid(row = 0,column=1)


    imagem = tk.PhotoImage(file="smm.png")
    lbImagem = tk.Label(janelaPrincipal, image=imagem)
    lbImagem.imagem = imagem
    lbImagem["height"] = 311
    lbImagem["width"] = 658
    lbImagem.grid(row=0, columnspan=300)

    botaoCadastrar = tk.Button(janelaPrincipal, width = 16, text = "Cadastrar Paciente", command = cadastrar_click, background = "White",highlightcolor = "White")
    botaoCadastrar.grid(row=2,column=1)

    botaoEditar = tk.Button(janelaPrincipal, width = 16, text = "Editar Paciente", command = editar_click, background = "White",highlightcolor = "White")
    botaoEditar.grid(row=2,column=2)

    botaoExcluir = tk.Button(janelaPrincipal, width = 16, text = "Excluir Paciente", command = editar_click, background = "White",highlightcolor = "White")
    botaoExcluir.grid(row=2,column=3)

    botaoMostrar = tk.Button(janelaPrincipal, width = 16, text = "Mostrar Paciente", command = editar_click, background = "White",highlightcolor = "White")
    botaoMostrar.grid(row=2,column=4)

    botaoEditar.mainloop()

construtorPrincipal()