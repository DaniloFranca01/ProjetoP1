import tkinter as tk
import tkinter.filedialog
from funcoesPacientes import *
def cadastrar_click():
    tkinter.FileDialog.telaCadastroPaciente
def editar_click():
    tkinter.FileDialog.telaCadastroPaciente

janelaPrincipal = tk.Tk()
janelaPrincipal.title("Medical Manager")
janelaPrincipal["bg"] = "#cbfbfe"
janelaPrincipal.geometry("800x400+300+300")
#bordaDireita  = tk.Label(janelaPrincipal, background = "Blue",height = 400).grid(row = 0,column=0)
#bordaEsquerda  = tk.Label(janelaPrincipal, background = "Blue",height = 400).grid(row = 0,column=1)



botaoCadastrar = tk.Button(janelaPrincipal, width = 16, text = "Cadastrar Paciente", command = cadastrar_click, background = "White",highlightcolor = "White")
botaoCadastrar.grid(row=2,column=1)

botaoEditar = tk.Button(janelaPrincipal, width = 16, text = "Editar Paciente", command = editar_click, background = "White",highlightcolor = "White")
botaoEditar.grid(row=2,column=2)

botaoExcluir = tk.Button(janelaPrincipal, width = 16, text = "Excluir Paciente", command = editar_click, background = "White",highlightcolor = "White")
botaoExcluir.grid(row=2,column=3)

botaoMostrar = tk.Button(janelaPrincipal, width = 16, text = "Mostrar Paciente", command = editar_click, background = "White",highlightcolor = "White")
botaoMostrar.grid(row=2,column=4)

botaoEditar.mainloop()