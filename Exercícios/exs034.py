#Escreva um programa que pergunte qual o sálario de um funcionário e calcule o valor do seu aumento. Para salários
#superiores a R$1250.00, calcule um aumento de 10%, para inferiores ou iguais um aumento de 15%.

salario = float(input('Qual o salário do funcionário em questão: '))

if salario <= 1250:
    print(f'O salário desse funcionário acrescido de um aumento de 15% passará a ser de R${salario*1.15:.2f}')
else:
    print(f'O salário desse funcionário acrescido de um aumento de 10% passará a ser de R${salario*1.10:.2f}')
