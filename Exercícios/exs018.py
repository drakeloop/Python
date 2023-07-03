#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import cos, tan, sin, radians

ang = float(input('Digite um ângulo qualquer: '))
angr = radians(ang)

print(f'Dado um ângulo de {ang}° possui:\nSeno {sin(angr):.3f};\nCosseno {cos(angr):.3f};\nTangente {tan(angr):.3f}.')
