operação = 1
maioridade = 0

while operação  !=0:
    idade = int(input('insira sua idade: '))
    if idade >=18:
        maioridade+=1

        operação = int(input('deseja sair? [0] para sim [1] para não'))
 
print('A quantidade de pessoas com 18 é de ', maioridade)


