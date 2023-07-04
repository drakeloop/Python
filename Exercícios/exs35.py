#Desenvolva um programa que leia três seguimentos de reta e diga ao usuário se elas podem ou não formar um triângulo:

r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))

if r1 + r2 < r3:
    print(f'Não é possivel formar um triângulo com essas retas. {r1} + {r2} > {r3}.')
elif r2 + r3 < r1:
    print(f'Não é possivel formar um triângulo com essas retas. {r2} + {r3} > {r1}.')
elif r3 + r1 < r2:
    print(f'Não é possivel formar um triângulo com essas retas. {r3} + {r1} > {r2}.')
else:
    print(f'Sim, podemos formar um triângulo com as retas {r1, r2, r3}.')
