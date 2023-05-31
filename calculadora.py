# Primeiramente as operações 

operacao = input('Digite: + para soma, - para subtração, * para multiplicação, / para divisão, sair para sair: ')

if operacao == '+':
    num1 = float(input('Qual o primeiro numero? '))
    num2 = float(input('Qual o segundo numero? '))
    soma = num1 + num2
    print(soma)
elif operacao == '-':
    num1 = float(input('Qual o primeiro numero? '))
    num2 = float(input('Qual o segundo numero? '))
    sub = num1 - num2
    print(sub)
elif operacao == '*':
    num1 = float(input('Qual o primeiro numero? '))
    num2 = float(input('Qual o segundo numero? '))
    mult = num1 * num2
    print(mult)
elif operacao == '/':
    num1 = float(input('Qual o primeiro numero? '))
    num2 = float(input('Qual o segundo numero? '))
    div = num1 / num2
    print(div)
else:
    print('Volte sempre!')