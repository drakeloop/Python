#Refaça o desafio exs051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão
#usando while.

prim = int(input('Primeiro Termo: '))
raz = int(input('Razão: '))
ult = prim + (raz * 10)

while prim < ult:
    print(prim, end='-->')
    prim += raz
