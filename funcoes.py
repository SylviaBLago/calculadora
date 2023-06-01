#função soma

def soma():
    quant = int(input('Quantos numeros deseja somar?' ))
    soma = 0
    i = 1

    while i < quant + 1:
        numero = float(input(f'Qual o numero {i} a ser somado? '))
        soma = soma + numero
        i = i + 1
        if i == quant + 1:
            print(f'A soma total é {soma}')


def subtracao():
    numero1 = float(input('Digite o número do qual deseja subtrair: '))
    numero2 = float(input('Digite o número a ser subtraido '))
    sub = numero1 - numero2
    continuar = input(f'O resultado da subtração é: {sub}. Deseja continuar a subtrair? ')

    while continuar == 'sim':
        numero3 = float(input('Digite o número a ser subtraido '))
        sub = sub - numero3
        continuar = input(f'O resultado da subtração é: {sub}. Deseja continuar a subtrair? ')
    if continuar == 'não':
        print(f'O resultado da sua subtração é {sub}. ')

def multiplicacao():
    num1 = float(input('Qual numero deseja multiplicar? '))
    num2 = float(input('Por qual numero deseja multiplicar? '))
    mult = num1 * num2

    continuar = input(f'O resultado da multiplicação é: {mult}. Deseja continuar multiplicando? ')
    while continuar == 'sim':
        num3 = float(input(f'Por qual numero deseja multiplicar {mult}? '))
        mult = mult * num3
        continuar = input(f'O resultado da multiplicação é: {mult}. Deseja continuar multiplicando? ')
    if continuar == 'não':
        print(f'O resultado da multiplicação é {mult}')

def divisao():
    num1 = float(input('Qual numero a ser dividido? '))
    num2  = float(input(f'Por quanto deseja dividir {num1}? '))
    div = num1/num2

    continuar = input(f'O resultado da divsão é: {div}. Deseja continuar dividindo? ')

    while continuar == 'sim':
        num3 = float(input(f'Por quanto deseja dividir {div}? '))
        div = div / num3
        continuar = input(f'O resultado da divsão é: {div}. Deseja continuar dividindo? ')
    if continuar == 'não':
        print(f'O resultado da sua divisão é {div}.')
