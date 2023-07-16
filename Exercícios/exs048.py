#Faça um programa que calcule a soma entre todos os números IMPARES que são múltiplos de 3 e que se encontram no
#intervalo ente 1 e 500.

soma = cont = 0

for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1
        soma += c
print(f'Entre 1 e 500 temos {cont} números múltiplos de 3, que somados juntos dão um total de {soma}.')
