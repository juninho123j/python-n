import mysql.connector

conecxão = mysql.connector.connect(
    host = 'localhost',
    port = 3306,
    user ='root',
    password='8446'
)
cursor = conecxão.cursor()
print('conectado com sucesso!')

print('''
     -------------------
    [sistema de cadastro] 
    [        de         ]
    [      alunos       ]
     ------------------- 
''')
alunos = []
quant_alunos = int(input('quantos alunos você quer registrar? '))
for _ in range(1):
    nomes = []
    for i in range(quant_alunos):
        nome = input('digite o nome do aluno: ')
        nomes.append(nome)
        alunos.append(nomes)
print(alunos)
print('''
    ----------------------  
    [Registre as notas e ]
    [    saiba a média   ]
    ----------------------
''')
cont = 0
quant_notas = int(input('quantas notas você vai cadastrar?  '))
notas = []
for _ in range(1):
    nota = [] 
    for i in range(quant_notas):  
        note = int(input('digite as notas: '))
        nota.append(note)
        notas.append(nota)
        for j in nota:
            if j >= 0:
                cont+=j
                result = cont/2   
            
print(notas)
for i in range(quant_alunos):
    cursor.execute('use escola')
    cursor.execute(f'insert into alunos (nome, nota, media ) values ("{nomes[0+i]}", "{nota[0 + i]}",{nota[0 + i]/2})')
    conecxão.commit()
cursor.execute("select nome, nota, media from alunos")
print([coluna[0] for coluna in cursor.description])
for linha in cursor.fetchall():
    print(linha)


