#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar 999,
#que é a condição de parada. No final mostre quantos números foram digitados e qual foia a soma entre eles.

num = int(input('[999]Parar. Digite um número inteiro: '))
cont = total = 0

while num != 999:
    total += num
    cont += 1
    num = int(input('[999]Parar. Digite um número inteiro: '))
print(f'A soma dos {cont} números digitdos é {total}')
