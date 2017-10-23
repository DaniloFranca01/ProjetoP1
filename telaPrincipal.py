import tkinter as tk
janelaLogin = tk.Tk()
janelaLogin.title("Medical Manager")
janelaLogin["bg"] = "#cbfbfe"
janelaLogin.geometry("800x400+300+300")
bordaDireita  = tk.Label(janelaLogin, background = "Blue",height = 400).grid(row = 0,column=0)
bordaEsquerda  = tk.Label(janelaLogin, background = "Blue",height = 400).grid(row = 0,column=1,sticky = NW)

janelaLogin.mainloop()