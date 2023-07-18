#Faça um programa que leia um número qualquer e mostre o seu fatorial: ex(5!=5x4x3x2x1=120)

num = int(input('Escolha um número para ver o fatorial: '))
f = 1
print(f'Calculando {num}! = ', end='')
while num != 0:
    print(num, end='')
    print(' X ' if num > 1 else ' = ', end='')
    f *= num
    num -= 1
print(f)
