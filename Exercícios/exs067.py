#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O
#programa deverá ser interrompido quando o valor for negativo.

while True:
    mult = 1
    num = int(input('Qual tabuada deseja ver: '))
    print('-='*20)
    if num < 0:
        break
    else:
        while mult <= 10:
            print(f'{num}  X {mult:2} = {num*mult:3}')
            mult += 1
        print('-=' * 20)
print('Programa encerrado!')
