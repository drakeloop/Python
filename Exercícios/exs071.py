#Crie um programa que simule o funcionamento de um caixa eletrônico. No inicio pergunte ao usuário qual o valor a ser
#sacado(número inteiro)e o programa irá informar quantas cédulas de cada valor serão entreges. obs(considere que o caixa
#tem cédulas de R$50 R$20 R$10 e R$1.

linha = '==' * 20

print(f'{linha}\n            Banco Sacada\n{linha}')
saque = int(input('Qual valor deseja sacar: R$'))
cinqenta = vinte = dez = um = 0

while True:
    if saque >= 50:
        saque -= 50
        cinqenta += 1
    if saque < 50 and saque >= 20:
        saque -= 20
        vinte += 1
    if saque < 20 and saque >= 10:
        saque -= 10
        dez += 1
    if saque < 10:
        saque -= 1
        um += 1
    if saque == 0:
        break
print(f'Cédulas de R$50: {cinqenta}\nCédulas de R$20: {vinte}\nCédulas de R$10: {dez}\nCédulas de R$1:  {um}')
