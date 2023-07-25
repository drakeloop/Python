#Crie um programa que vai gerar 5 números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números
#gerados e também indique o maior e o menor valor que estão na tupla.

from random import randint

nums = (randint(1, 50), randint(1, 50), randint(1, 50), randint(1, 50), randint(1, 50))
ord = sorted(nums)

print(f'Os números gerados foram os {nums}')
print(f'Sendo o Maior número: {ord[-1]}\nE o Menor número: {ord[0]} ')
