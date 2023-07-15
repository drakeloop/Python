#A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
#categoria, de acordo com a idade: -Até 6 anos: Mirim, -Até 11 anos:Infantil, -Até 19 anos:Junior, -Até 24:Sênior,
#-Acima de 26 anos:Master.

from datetime import date
nasc = int(input('Data de nascimento: '))
idade = date.today().year - nasc

if idade < 6:
    print(f'Categoria: Atleta MIRIM')
elif idade >= 6 and idade < 11:
    print(f'Categoria: Atleta INFANTIL')
elif idade >= 11 and idade < 19:
    print(f'Categoria: Atleta JÚNIOR')
elif idade >= 19 and idade < 26:
    print(f'Categoria: Atleta SÊNIOR')
elif idade >= 26:
    print(f'Categoria: Atleta MASTER')