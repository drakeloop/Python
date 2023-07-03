#Faça um programa que leia um número entre 0 e 9999 e mostre na tela cada um de seus digitos separados por unidade,
#dezena, centena e milhar.

num = int(input('Digite um número entre 0 e 9999: '))
num = num+10000
num = str(num)

print(f'Milhar: {num[-4]}')
print(f'Centena: {num[-3]}')
print(f'Dezena: {num[-2]}')
print(f'Unidade: {num[-1]}')

#-----------------------------------ou-----------------------------------
'''
    Veja os exemplos abaixo.
    Divisão: 1234 / 10 = 123,4
    Divisão inteira: 1234 //10 = 123
    Módulo: 1234 % 10 = 4
    Pra ele descobrir a centena ele faz isso:
    Faz a divisão inteira por 100: 1234 // 100 = 12
    Depois pega o resultado e dividi por 10,mas pega só o resto dessa 
    divisão (que é o módulo): 12 % 10 = 2
    Ou seja, a centena é 2.
'''
