#Faça um nome que leia o nome completo de uma pessoa, mostrando em seguida separadamente o primeiro e o último nome.

nome = str(input('Digite o seu nome completo: ')).title().split()

print(f'Seu primeiro nome é {nome[0]}')
print(f'E o último nome é {nome[-1]}')