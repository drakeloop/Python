#Escreva um programa que leia um número inteiro qualquer e peça para o úsuario escolher qual será a base de conversão:
#1-Binário, 2-octal e 3-hexadecimal.

num = int(input('Digite um número inteiro: '))
conv = int(input('Escolha a conversão desejada: \n[ 1 ] Binário \n[ 2 ] Octal \n[ 3 ] Hexadecimal \nEscolha: '))

if conv == 1:
    print(f'O número {num} em Binário tem o valor de {bin(num)[2:]}')
elif conv == 2:
    print(f'O número {num} em Octal tem o valor de {oct(num)[2:]}')
elif conv == 3:
    print(f'O número {num} em Hexadecímal tem o valor de {hex(num)[2:]}')
else:
    print(f'Opção invalída.')