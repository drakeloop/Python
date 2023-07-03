#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele
#foi multado. A multa vai custar R$7.00 por km acima do limite.

velo = int(input('Qual foi a velocidade do veículo em Km/h: '))
print('---'*20)

if velo <= 80:
    print('Parábens! Você está dentro da velocidade permitida.')
else:
    print(f'Ops, você ultrapassou o limite de velocidade em {velo - 80}Km/h')
    print(f'Você deve pagar uma multa de R${(velo - 80)*7:.2f} reais.')
    print('Tome mais cuidado com o limite de velocidade!')
    