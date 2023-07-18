#Crie um programa que leia dois valores e mostre um menu na tela: -somar, -multiplicar, -maior, -novos números e
#-encerrar programa. Seu programa deverá executar a função em cada opção solicitada.

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
linha = '__' * 30

op = 0
while op != 5:
    print(linha)
    op = int(input('[ 1 ]Somar'
                   '\n{ 2 ]Multiplicar'
                   '\n[ 3 ]Maior'
                   '\n[ 4 ]Novos números'
                   '\n[ 5 ]Encerrar o programa'
                   '\nOpção: '))
    print(linha)
    if op == 1:
        print(f'A soma de {n1} + {n2} = {n1+n2}')
    if op == 2:
        print(f'A multiplicação de {n1} X {n2} = {n1*n2}')
    if op == 3:
        if n1 > n2:
            print(f'O número {n1} é maior que o {n2}')
        elif n1 < n2:
            print(f'O npumero {n2} é maior que o {n1}')
        elif n1 == n2:
            print(f'Os numeros são ambos iguais {n1}')
    if op == 4:
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
print('Programa Encerrado')
