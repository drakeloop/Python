#Desenvolva um programa que pergunte a distância de uma viagem em quilômetros. Calcule o preço da passagem, cobrando
#R$0.50 por Km para viagens de até 200Km e R$0.45 para viagens mais longas.

distancia = float(input('Digite a distŝncia da sua viagem em Km: '))

if distancia <= 200:
    print(f'Com base na distância da sua viagem, o preço da passagem será de R${distancia*0.50:.2f}')
else:
    print(f'Com base na distância da sua viagem, o preço da passagem será de R${distancia*0.45:.2f}')
