#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade: -Se ele vai se alistar
#no serviço militar. -Se já é a hora de ele se alistar ou -Se ele está com o alistamento atrasado.
#Seu programa também deverá mostrar quanto tempo falta ou passou do alistamento.

from datetime import date
nasc = int(input('Data de nascimento: '))
idade = date.today().year - nasc

if idade < 18:
    print(f'Você ainda tem {idade} anos, seu alistamento será em {18-idade} ano(s).')
elif idade == 18:
    print(f'Você já tem {idade} anos, procure a junta militar mais próxima ou acesse o site www.ExercitoBrasileiro/alistamento.com.br ')
elif idade > 18:
    print(f'Você já tem {idade} anos, seu alistamento está atrasado em {idade - 18} ano(s).')
    print('Procure a junta militar mais próxima ou acesse o site www.ExercitoBrasileiro/alistamento.com.br para esclarecimento.')