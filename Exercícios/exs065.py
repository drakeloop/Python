#Crie um programa que leia vários números inteiros pelo teclado. No final da execução mostre a média entre todos os
#valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar
#digitando os valores.

seguir = 'S'
cont = total = maior = menor = 0

while seguir == 'S':
    num = int(input('Digite um número: '))
    cont += 1
    total += num
    if cont == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    seguir = str(input('Continuar digitando número? [S/N]')).upper().strip()[0]
print(f'Você digitou {cont} números e a média foi {total/cont}')
print(f'O maior número coletado foi {maior} e o menor foi {menor}')
