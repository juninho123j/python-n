caluladora = 1

while caluladora != 0:

    operacao = str(input('qual operação deseja realizar ?'\
                         'Digite [/] divisão'\
                         'Digite [*] multiplicar'\
                         'Digite [+] para somar'))                         
    if operacao == "/":
        n1 = float(input('digite um numero ?'))
        n2 = float(input('digite outro numero ?'))
        resultado = n1/n2
        print(resultado)
    if operacao == '*':
        resultado = n1 * n2
        print(resultado)
    else:
        resultado = n1 + n2


