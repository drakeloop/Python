#Faça um programa que leia 6 números inteiros e mostre apenas aqueles que forem pares. Se o valor digitado for ímpar
#desconsidere-o.

somap = 0

for c in range(1, 7):
    n = int(input(f'Digite o {c}° número: '))
    if n % 2 == 0:
        somap += n
print(f'A soma dos números pares coletados é de {somap}')
