#Crie um programa que leia o nome completo de uma pessoa e mostre:
#-O nome com todas letras maiúsculas;
#-O nome com todas as letras minúsculas;
#-Quantas letras ao tod(o) sem considerar os espaços;
#-Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome completo: '))
nomej = nome.split()

print(f'Todo maiúsculo: {nome.upper()}')
print(f'Todo minúsculo: {nome.lower()}')
print(f'Quantidade total de letras: {len("".join(nomej))} letras')
print(f'Quantidade de letras do primeiro nome: {len(nomej[0])} letras')

