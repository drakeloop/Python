#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela sua porção inteira.
#ex:6.127 tem sua porção inteira 6.

from math import floor
num = float(input('Digite um número com ponto flutuante: '))

print(f'O número {num} tem sua porção inteira {floor(num)}.')
