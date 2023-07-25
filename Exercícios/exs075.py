#Desenvolva um programa que leia quatro números pelo teclado e guarde-os em uma tupla, no final mostre: -Quantas vezes
#apareceu o valor 9, -Em que posiçâo foi digitado o primeiro valor 3, -Quais foram os números pares.

n1 = int(input('Digite o número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))
n3 = int(input('Digite mais um número inteiro: '))
n4 = int(input('Digite o último número inteiro: '))
numeros = (n1, n2, n3, n4)
par = ()

print(f'O valor 9 apareceu {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O primeiro 3 foi digitado na {numeros.index(3)+1}ª posição')
else:
    print(f'O número 3 não apareceu em nenhuma posição')
print(f'Os números pares digitados foram: ', end='')
for num in numeros:
    if num % 2 == 0:
        print(num, end=' ')

