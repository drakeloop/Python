#Escreva um programa que leia um número inteiro e mostre na tela se ele é impar ou par.

num = int(input('Digite um número inteiro: '))

if num % 2 == 0:
    print(f'O número {num} é um número par.')
else:
    print(f'O número {num} é um número impar.')
