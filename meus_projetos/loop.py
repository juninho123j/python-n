from tkinter import *

janela = Tk()
janela.title('frequencia')
janela.geometry('500x600')

tela = Label(janela, text='digite sua frequencia')
tela.pack(side=TOP)


frequencia = Entry(janela)
frequencia.pack(side=TOP)

mostrar_frequencia = Label(janela, text='')
mostrar_frequencia.pack(side=TOP)

def frequencia():
   try:
      frequencia = int(frequencia.get())
      n = f'{frequencia + 1}'
      mostrar_frequencia['text'] = n
   except ValueError:
      mostrar_frequencia['text'] = 'ruim'

botão = Button (janela, text='veja sua frequencia', command=frequencia)
botão.pack(side=TOP)


janela.mainloop()
