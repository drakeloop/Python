#Refeça o desafio exs035 dos triângulos, acrescentando o recurso de mostrar qual tipo de triângulo será formado:
#-Equiláteros: Todos os lados iguais. -Isóceles: Dois lados iguais, e -Escaleno: Todos os lados diferentes.

print('Indique 3 seguimentos de retas e veja qual tipo de triângulo será formado.')
r1 = float(input('Reta 1: '))
r2 = float(input('Reta 2: '))
r3 = float(input('Reta 3: '))

if r1 + r2 < r3:
    print(f'Não é possivel formar um triângulo com essas retas. {r1} + {r2} < {r3}.')
elif r2 + r3 < r1:
    print(f'Não é possivel formar um triângulo com essas retas. {r2} + {r3} < {r1}.')
elif r3 + r1 < r2:
    print(f'Não é possivel formar um triângulo com essas retas. {r3} + {r1} < {r2}.')

else:
    print(f'Sim, podemos formar um triângulo com as retas')
    if r1 == r2 and r2 == r3:
        print(f'As retas {r1}, {r2} e {r3} formaram um triângulo EQUILÁTERO.')
    elif r1 == r2 and r2 != r3 or r2 == r3 and r2 != r1 or r3 == r1 and r2 != r3:
        print(f'As retas {r1}, {r2} e {r3} formaram um triângulo ISÓCELES.')
    else:
        print(f'As retas {r1}, {r2} e {r3} formaram um triângulo ESCALENO.')
