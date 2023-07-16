#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas e no final mostre:
#-A média de idade do grupo
#-O nome do homem mais velho
#-Quantas mulheres tem menos de 21

velho = ''
idvelho = menores = media = 0

for pessoa in range(1, 5):
    print(f'--------{pessoa}° PESSOA----------')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [F/M]: ')).strip().upper()

    if idade:
        media += idade
    if sexo == 'M':
        if pessoa == 1:
            idvelho = idade
            velho = nome
        else:
            idade > idvelho
            idvelho = idade
            velho = nome
    if sexo == 'F':
        if idade < 21:
            menores += 1

print(f'A média de idade do grupo é {media/4} de idade.')
print(f'O homem mais velho é o Sr.{velho} com {idvelho} anos.')
print(f'Mulheres menores no grupo: {menores}')
