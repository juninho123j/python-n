from tkinter import *

janela = Tk()
janela.title('tabuada')
janela.geometry('300x200')

tabuada = Label(janela, text= 'digite um numero para ver sua tabuada :')
tabuada.pack( side=TOP)

num = Entry(janela)
num.pack(side=TOP)

tabuada2 = Label(janela, text= '')
tabuada2.pack( side=TOP)

    
def mostrar_tabuada():
    try:
        numero = int(num.get())
        n = f'{numero} x {1} = {numero*1} \n{numero} x {2} = {numero*2} \n{numero} x {3} = {numero*3} \n{numero} x {4} = {numero*4} \n{numero} x {5} = {numero*5} \n{numero} x {6} = {numero*6} \n{numero} x {7} = {numero*7} \n{numero} x {8} = {numero*8} \n{numero} x {9} = {numero*9} \n{numero} x {10} = {numero*10}'
        tabuada2['text'] = n
    except ValueError:
        tabuada2['text'] = 'Por favor, digite um número válido.'

botão = Button(janela, text='ver tabuada', command=mostrar_tabuada)
botão.pack( side=TOP)
janela.mainloop()
    
