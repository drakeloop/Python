#Faça um programa que mostre na tela uma contagem regressiva para estourar os fogos de artíficios, indo de 10 à 0 com
#pausas de 1 segundo entre eles.

from time import sleep

print(f'Vamos começar a contagem regressíva, para a queima de fogos! 🎆')
sleep(3)

for c in range(10, 0, -1):
    print(f'{c}...')
    sleep(1)
print('🎆🎆 Feliz Ano Novo! 🎆🎆')
sleep(1)
print('Bum! 🎆')
sleep(1)
print('🎆 Katchau 🎆')
