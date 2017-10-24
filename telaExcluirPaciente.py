import tkinter as tk
import tkinter.messagebox
import funcoesPacientes as fpc
def button_click():
    tk.messagebox.showinfo("ATENÇÃO","Deseja excluir o paciente: ?")
    fpc.excluirPaciente(edCpf.get())

janeExcluirPaciente = tk.Tk()
janeExcluirPaciente.title("Excluir paciente")
janeExcluirPaciente["bg"] = "#cbfbfe"

lbCpf = tk.Label(janeExcluirPaciente, text="CPF: ")
lbCpf.grid(row = 1)
lbCpf["bg"] = "#cbfbfe"
edCpf = tk.Entry(janeExcluirPaciente)
edCpf.grid(row = 1,column = 2)
botaoCadastrar = tk.Button(janeExcluirPaciente, width = 16, text = "Excluir", command = button_click, background = "White",highlightcolor = "White")
botaoCadastrar.grid(row=2,column = 2)

janeExcluirPaciente.mainloop()