#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar 999,
#que é a condição de parada. No final mostre quantos números foram digitados e qual foia a soma entre eles.
#Só que usando break.
cont = total = 0

while True:
    num = int(input('[999]Parar. Digite um número inteiro: '))
    if num == 999:
        break
    else:
        total += num
        cont += 1
print(f'A soma dos {cont} números digitdos é {total}')
