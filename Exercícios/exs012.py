#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5%  de desconto.

valor = float(input('Digite o valor do produto? '))

print(f'O produto de R${valor} com desconto de 5% passará a custar R${valor*0.95:.2f}')
