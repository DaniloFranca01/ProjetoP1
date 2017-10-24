import tkinter as tk
from funcoesPacientes import *
def cadastrar_click():
    tk.FileDialog.telaCadastroPaciente
def editar_click():
    tk.FileDialog.telaCadastroPaciente

janelaPrincipal = tk.Tk()
janelaPrincipal.title("Medical Manager")
janelaPrincipal["bg"] = "#cbfbfe"
janelaPrincipal.geometry("800x400+300+300")
#bordaDireita  = tk.Label(janelaPrincipal, background = "Blue",height = 400).grid(row = 0,column=0)
#bordaEsquerda  = tk.Label(janelaPrincipal, background = "Blue",height = 400).grid(row = 0,column=1)

menubar = tk.Menu(janelaPrincipal)
janelaPrincipal.config(menu=menubar)
filemenu = tk.Menu(menubar)
filemenu2 = tk.Menu(menubar)
menubar.add_cascade(label='Arquivo', menu=filemenu)
menubar.add_cascade(label='Gerenciamento', menu=filemenu2)
menubar.grid(row=1,column=1)

botaoCadastrar = tk.Button(janelaPrincipal, width = 16, text = "Cadastrar Paciente", command = cadastrar_click, background = "White",highlightcolor = "White")
botaoCadastrar.grid(row=2,column=1)

botaoEditar = tk.Button(janelaPrincipal, width = 16, text = "Editar Paciente", command = editar_click, background = "White",highlightcolor = "White")
botaoEditar.grid(row=2,column=2)

botaoEditar.mainloop()