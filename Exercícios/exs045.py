#Crie um programa que faça o computador jogar Jokenpô com o usuário.

from time import sleep
from random import randint

print('Vamos jogar Jokenpô! ')
pc = randint(1, 3)
print('Escolha entre: \n[ 1 ]Pedra \n[ 2 ]Papel \n[ 3 ]Tesoura')
sleep(0.7)
usuario = int(input('JOKEN... '))
