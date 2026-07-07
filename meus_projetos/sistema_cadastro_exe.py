from tkinter import *
import tkinter as tk
import mysql.connector
conecxão = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '8446',
    port = '3306',
    database = 'cadastro'
)

print('conecxão bem sucedida')
cursor = conecxão.cursor()

janela = Tk()
janela.title("Sistema de Cadastro")
janela.geometry('800x720')
Label(janela, text='sistema de cadastro', font=('arial', 14)).pack(side=TOP)

Label(janela, text='NOME:').pack(side=TOP)
entrada_nome = Entry(janela, width=20)
entrada_nome.pack(side=TOP)

Label(janela, text='RA:').pack(side=TOP)
entrada_RA = Entry(janela, width=20)
entrada_RA.pack(side=TOP)

Label(janela, text='NOTA:').pack(side=TOP)
entrada_nota = Entry(janela, width = 20)
entrada_nota.pack(side=TOP)

Label(janela, text='DATA(ex: ano-mes-dia):').pack(side=TOP)
entrada_data = Entry(janela, width=20)
entrada_data.pack(side=TOP)

def cadastrar():
    nome = str(entrada_nome.get())
    ra = float(entrada_RA.get())
    nota = float(entrada_nota.get())
    data = str(entrada_data.get())
    cursor.execute(f'Insert into cadastro (nome, RA, nota, dia) Value ("{nome}", {ra}, {nota}, "{data}" )')
    conecxão.commit()
    Label(janela, text='cadatrado com sucesso').pack(side=TOP)
def alunos_cadastrados():
    janela2 = Toplevel()
    janela2.title('sistema de cadastro')
    janela2.attributes('-fullscreen', True)
    cursor.execute('use cadastro')
    cursor.execute('SELECT id, nome, RA, nota , dia from cadastro')
    Label(janela2, text=f'id | NOME   |      RA         | NOTA |    DATA',font=('arial', 20)).pack(side=TOP) 
    for linha in cursor.fetchall():
        id = linha[0]
        nome = linha[1]
        nota = float(linha[2])
        ra = linha[3]
        data = (linha[4].strftime('%d/%m/%y'))
        Label(janela2, text=f'{id} | {nome} | {ra} | {nota}  | {data}', font=('arial', 20)).pack(side=TOP)
    Label(janela2, text='digite o RA do aluno que vc quer excluir:').pack(side=TOP)
    entrada_alunos = Entry(janela2)
    entrada_alunos.pack(side=TOP)
    def delete_alunos():
        deletar = float(entrada_alunos.get())
        cursor.execute(f'DELETE from cadastro where ra = {deletar} ')
        conecxão.commit()
        janela2.update()
    def carregar_alunos():
        janela2.destroy()
        alunos_cadastrados()
    atualizar = Button(janela2, text='atualizar', command=carregar_alunos)
    atualizar.pack(side=TOP)
    excluir_alunos = Button(janela2, text='Deletar', command= delete_alunos)
    excluir_alunos.pack(side=TOP)
    def fechar():
        janela2.destroy()
    fechar_janela = Button(janela2, text='fechar', command=fechar)
    fechar_janela.pack(side=TOP)
    janela2.mainloop()
    
lista_de_alunos = Button(janela, text='ver lista de alunos', command=alunos_cadastrados)
lista_de_alunos.pack(side=TOP)
Button(janela, text='cadastrar', command=cadastrar).pack(side=TOP)
janela.mainloop()