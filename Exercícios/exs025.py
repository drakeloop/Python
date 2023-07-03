#Crie um programa que leia o nome de uma pessoa e diga se tem 'Silva' nele.

nome = str(input('Digite seu nome completo: ')).strip().title()

print(f'O nome {nome}, tem "Silva" no nome: {"Silva" in nome}')
