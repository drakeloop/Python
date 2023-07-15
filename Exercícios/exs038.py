#Escreva um programa que leia dois números inteiros e compare-os mostrando uma mensagem na tela:
#-O primeiro valor é maior - o segundo valor é maior -Não existe valor maior, ambos valores são iguais.

n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))

if n1 > n2:
    print(f'O número {n1} é Maior que o número {n2}')
elif n2 > n1:
    print(f'O número {n2} é maior que o número {n1}')
else:
    print(f'Não existe número maior ambos números são iguais {n1}')
