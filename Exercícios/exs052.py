#Faça um programa que leia um número inteiro e mostre se ele é ou não um número primo:

num = int(input('Digite um número: '))
cont = 0

for c in range(1, num+1):
    if num % c == 0:
        cont += 1
if cont == 2:
    print(f'O número {num} é um número primo, apenas divísivel por ele mesmo e por 1.')
else:
    print(f'O número {num} é divisível por {cont} números, então não é um número primo.')
