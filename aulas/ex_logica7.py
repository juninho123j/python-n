nota1 = float(input('digite a nota :'))
nota2 = float(input('digite a nota :'))
nota3 = float(input('digite a nota :'))
nota4 = float(input('digite a nota :'))

result = (nota1 + nota2 + nota3 + nota4)/4

if result >=7:
    print(f'sua média é de {result:.1f} aprovado')
else:
    print(f'sua média é de {result:.1f} reprovado')