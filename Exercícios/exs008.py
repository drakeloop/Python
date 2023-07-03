#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e mílimetros.

metros = float(input('Digite a medida em metros: '))

print(f'Uma medida de {metros:.0f} metros:\nTem {metros*100:.0f} centimetros;\nTem {metros*1000:.0f} milímetros')
