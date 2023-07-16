#Refaça o desafio exs009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando o laço for.

num = int(input('Qual tabuada deseja ver: '))

for c in range(1, 11):
    print(f'{num}  X {c:2} = {c*num:2}')
