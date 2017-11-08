import tkinter as tk
import tkinter.messagebox
import funcoesPacientes as fpc
def construtorDelFacientes():
    def button_click():
        tk.messagebox.showinfo("ATENÇÃO","Deseja excluir o paciente: ?")
        fpc.excluirPaciente(edCpf.get())

    janelaExcluirPaciente = tk.Tk()
    janelaExcluirPaciente.title("Excluir paciente")
    janelaExcluirPaciente["bg"] = "#cbfbfe"
    janelaExcluirPaciente.geometry("250x100+300+300")

    lbCpf = tk.Label(janelaExcluirPaciente, text="CPF: ")
    lbCpf.grid(row = 1)
    lbCpf["bg"] = "#cbfbfe"
    edCpf = tk.Entry(janelaExcluirPaciente)
    edCpf.grid(row = 1,column = 2)
    botaoCadastrar = tk.Button(janelaExcluirPaciente, width = 16, text = "Excluir", command = button_click, background = "White",highlightcolor = "White")
    botaoCadastrar.grid(row=2,column = 2)

    janelaExcluirPaciente.mainloop()