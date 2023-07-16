#Crie um programa que leia a data de nascimento de sete pessoas. No final mostre quantas pessoas ainda não atingiram a
#maioridade e quantas são de maior.

from datetime import date
maior = menor = 0

for c in range(1, 8):
    nasc = int(input('Data de nascimento: '))
    idade = date.today().year - nasc

    if idade >= 21:
        maior += 1
    else:
        menor += 1
print(f'Entre as sete pessoas em questão: São menores de 21 anos: {menor} \nSão maiores de 21 anos: {maior}.')
