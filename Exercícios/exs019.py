#Um professor quer sortear um de seus 4 alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles
#e mostrando o nome do escolhido.

from random import choice
a1 = str(input('Nome do primeiro aluno: ')).title()
a2 = str(input('Nome do Segundo aluno: ')).title()
a3 = str(input('Nome do Terceiro aluno: ')).title()
a4 = str(input('Nome do quarto aluno: ')).title()

nomes = (a1, a2, a3, a4)

print(f'Dentre os seguintes alunos: {nomes}\nO escolhido para apagar o quadro foi: {choice(nomes)}')
