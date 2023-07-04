#Faça um programa que leia um ano qualquer e diga se ele é um ano bissexto ou não.

from datetime import date
ano = int(input('Digite um ano qualquer: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'{ano} - É um ano Bissexto')
else:
    print(f'{ano} - Não é um ano Bissexto')
