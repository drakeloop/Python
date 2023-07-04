#Faça um programa que leia 3 números e mostre qual é o maior e qual é o menor entre eles.

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

if n1 > n2 and n1 > n3:
    print(f'O Número {n1} é o maior número.')
if n1 < n2 and n1 < n3:
    print(f'O Número {n1} é o menor número.')

if n2 > n3 and n2 > n1:
    print(f'O Número {n2} é o maior número.')
if n2 < n3 and n2 < n1:
    print(f'O Número {n2} é o menor número.')

if n3 > n2 and n3 > n1:
    print(f'O Número {n3} é o maior número.')
if n3 < n2 and n3 < n1:
    print(f'O Número {n3} é o menor número.')
