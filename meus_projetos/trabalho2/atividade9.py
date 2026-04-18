num = 1
quant = 0

while num !=0:
    num2 = int(input('digite um numero: '))
    if num2 >=0:
        quant+=1
        num = int(input('digite [0] pra sair [1] pra continuar'))
print('a quantidade de numero diferente de 0 é : ', quant)


