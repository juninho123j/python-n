from tkinter import *
import tkinter as tk

janela = Tk()
janela.title("Ferro Velho") 
janela.geometry("500x400")
janela.configure(bg='gray')
va = 0 
entrada = Entry(janela, font=('Arial', 14))
entrada.pack(pady=20)
def valor():
    global va
    try:
        valor1 = float(entrada.get())
        va += valor1 
        f.config(text=f"Valor total: R${va:.2f}", font=('Arial', 20), fg='black')
        entrada.delete(0, END)
    except ValueError:
            f.config(text="Por favor, coloque um ponto", font=('Arial', 20), fg='black')
            return
        
               
f = Label(janela, text='', bg='gray')
f.pack(side=TOP)

calcular = Button(janela, text="Calcular", command=valor)
calcular.pack(pady=10)
    

janela.mainloop()
