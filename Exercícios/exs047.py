#Crie um programa que mostre na tela todos os números pares que estão entre 1 e 50.

from time import sleep
for c in range(1, 50):
    if c % 2 == 0:
        print(f'{c}', end=' --> ')
        sleep(0.5)
print('FIM')
