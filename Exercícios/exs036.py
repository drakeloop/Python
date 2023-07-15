#Escreva um programa para aprovar um empréstimo bancário para comprar uma casa. O programa deverá perguntar o valor da
#casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que ela não
#pode exceder 30% do salário ou então o empréstimo será negado.

casa = int(input('Valor da casa: R$'))
salario = int(input('Salário: R$'))
anos = int(input('Em quantos anos deseja pagar: '))

meses = anos * 12

if salario*0.3 > casa / meses:
    print(f'Seu empréstimo de R${casa:.2f} foi feito em {meses} parcelas de R${casa/meses:.2f}')
else:
    print(f'Seu empréstimo não foi aprovado pois as parcelas de R${casa/meses:.2f} ultrapassam 30% do seu salário.')