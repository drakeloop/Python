#Faça um programa que jogue ímpar ou par com o computador. O jogo só deverá parar quando o jogador PERDER, mostrando o
#total de vitórias que ele conquistou até o final do jogo.

from random import randint
print('Vamos jogar ímpar ou par!')
vit = 0

while True:
    comp = randint(1, 10)
    ioup = str(input('Impar ou Par [I/P]: ')).strip().upper()[0]
    jog = int(input('Escolha um número: '))
    if ioup == 'I':
        if (comp + jog) % 2 == 0:
            print(f'Perdeu eu escolhi o número {comp} deu {comp+jog}')
            break
        if (comp + jog) % 2 > 0:
            print(f'Você venceu a rodada! Eu escolhi o número {comp} deu {comp+jog}')
            print('Vamos denovo!')
            vit += 1
    if ioup == 'P':
        if (comp + jog) % 2 == 0:
            print(f'Você venceu a rodada! Eu escolhi o número {comp} deu {comp + jog}')
            print('Vamos denovo!')
            vit += 1
        if (comp + jog) % 2 > 0:
            print(f'Perdeu eu escolhi o número {comp} deu {comp + jog}')
            break
print(f'Você venceu {vit} vezes seguidas.')
