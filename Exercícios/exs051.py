#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final mostre os 10 primeiros termos dessa
#progressão.

print('Vamos fazer uma Progressão Aritimética.')
pri = int(input('Primeiro termo: '))
raz = int(input('Razão: '))
ult = pri + (raz*10)

for c in range(pri, ult, raz):
    print(f'{c}', end=' --> ')
print('FIM.')