#Crie um programa que leia a idade e o sexo de várias pessoas, a cada pessoa cadastrada o programa deverá perguntar se
#o usuário quer ou não continuar. No final mostre: -quantas pessoas tem mais de 18 anos, -quantos homens foram
#cadastrados, -quantas mulheres tem menos de 20 anos.

while True:
    print('--' * 20)
    print('CADASTRE UMA PESSOA')
    print('--' * 20)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo[M/F]: ')).strip().upper()[0]
    cont = str(input('Quer continuar?[S/N]: ')).strip().upper()[0]
    if cont in 'N':
        break
    print('===== Programa Encerrado ======')
