#Crie um programa que leia a idade e o sexo de várias pessoas, a cada pessoa cadastrada o programa deverá perguntar se
#o usuário quer ou não continuar. No final mostre: -quantas pessoas tem mais de 18 anos, -quantos homens foram
#cadastrados, -quantas mulheres tem menos de 20 anos.
maiores = homens = mmenores = 0

while True:
    print('--' * 20)
    print('CADASTRE UMA PESSOA')
    print('--' * 20)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo[M/F]: ')).strip().upper()[0]
    if idade >= 18:
        maiores += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mmenores += 1

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar?[S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print('===== Programa Encerrado ======')
print('Com base nos dados levantados nesse grupo, temos:')
print(f'Maiores de 18 anos: {maiores}'
      f'\nHomens cadastrados: {homens}'
      f'\nMulheres menores de 20 anos: {mmenores}')
