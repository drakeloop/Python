#Melhore o jogo do desafio exs028 onde o computador vai 'pensar' em um número de 0 a 10. Só que agora o jogo vai tentar
#adivinhar até acertar. Mostrando no final quantos palpites foram necessários para vencer.

from random import randint
from time import sleep

cont = 0
comp = randint(1, 10)
print('Vamos jogar um jogo! Vou pensar em um número entre 0 e 10...')
sleep(2)
print('Pensando...')
sleep(2)
print('Já sei... esse mesmo!')
sleep(2)

acertou = False
while not acertou:
    cont += 1
    jogador = int(input('Adivinhe em qual número eu pensei de 0 á 10: '))
    if jogador > comp:
       print(f'Errouuuu! Meu número é MENOR.{comp}')
    if jogador < comp:
        print(f'Errouuuu! Meu número é MAIOR.{comp}')
    if jogador == comp:
        print(f'Parabéns! Você acertou depois de {cont} tentativas.')
        acertou = True
