from tkinter import *
import tkinter as tk

janela = Tk()
janela.title("Ferro Velho") 
janela.geometry("500x400")
janela.configure(bg='gray')
entrada = Entry(janela, font=('Arial', 14))
entrada.pack(pady=20)
valor1 = 0
def valor():
    global valor1
    try:
        va = float(entrada.get())
        valor1 += va
        f.config(text=f"Valor total: R${valor1:.2f}", font=('Arial', 20), fg='black')
        entrada.delete(0, END)
    except ValueError:
        f.config(text="Por favor, coloque um ponto", font=('Arial', 20), fg='black')



f = Label(janela, text='', bg='gray')
f.pack(side=TOP)

cal = Button(janela, text="Calcular", command=valor)
cal.pack(pady=10)

janela.mainloop()
