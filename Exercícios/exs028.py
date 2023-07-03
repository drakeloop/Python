#Escreva um programa que faça o computador 'pensar' Em um número inteiro entre 0 e 5 e peça para o usuário tentar
#descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o úsuario venceu ou
#perdeu.

from random import randint
from time import sleep

comp = randint(0, 5)
print('Vamos jogar um jogo! Vou pensar em um número entre 0 e 5...')
sleep(2)
print('Pensando...')
sleep(2)
print('Já sei... esse mesmo!')
sleep(2)

jogador = int(input('Adivinhe em qual número eu pensei de 0 á 5: '))

print('Processando...')
sleep(1.5)
print('Processando...')
sleep(1.5)

if jogador == comp:
    print(f'Parabéns, você acertou eu realmente pensei no número {comp}.')
else:
    print(f'Oou... Você errou eu pensei no número {comp}.')
