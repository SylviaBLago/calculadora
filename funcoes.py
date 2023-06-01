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
        print(f'O resultado da sua subtração é {sub}. Recarregue a página para recomeçar. ')

subtracao()   

        
