#Faça um programa que leia o peso de 5 pessoas e mostre qual foi o maior e o menor peso lido.

maiorp = menorp = 0

for pessoa in range(1, 6):
    peso = float(input(f'Peso da {pessoa}°Pessoa: '))

    if pessoa == 1:
        maiorp = peso
        menorp = peso
    else:
        if peso > maiorp:
            maiorp = peso
        if peso < menorp:
            menorp = peso
print(f'No grupo a pessoa mais pesada tem {maiorp:.1f}Kg e a pessoa mais leve tem {menorp}Kg.')
