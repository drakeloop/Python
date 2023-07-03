#Faça um programna que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e
#mostre o comprimento da hipotenusa.

from math import sqrt, pow
co = float(input('Cateto Oposto: '))
ca = float(input('Cateto Adjacente: '))

print(f'O Triângulo Retângulo de Cateto Oposto de {co} e Cateto Adjacente de {ca},\ntem sua hipotenusa com '
      f'{sqrt(ca**2+co**2):.2f} de comprimento.')
