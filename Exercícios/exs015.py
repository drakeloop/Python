#Escreva um programa que pergunte a quantidade de quilômetros percorridos por um carro alugado e a quantidade de dias
#pelo quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60,00 reais por dia alugado e R$0,15
#por Km rodado.

dias = int(input('Por quantos dias o carro foi alugado: '))
km = int(input('Quantos quilômetros foram rodados nesses dias: '))

diarias = dias * 60
rodados = km * 0.15
print(f'O Aluguel de {dias} dias mais o valor referente a {km}Km rodados, \nDeu um total de R${diarias+rodados:.2f} '
      f'reais a serem pagos.')
