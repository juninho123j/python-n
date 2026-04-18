num = 1

while num !=0:
   nome = input('digite seu nome:')

   idade = int(input('digite sua idade: '))
   num = int(input('digite [0] pra sair [1] pra continuar'))
   if idade >=18:
    print('maior de idade')
   else:
    print('menor de idade')

    