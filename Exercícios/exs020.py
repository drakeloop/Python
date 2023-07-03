#O mesmo professor do desafio anterior quer sortear a ordem de apresentação dos trabalhos dos alunos. Faça um programa
#que leia o nome dos alunos e sorteie a ordem de apresentação.

a1 = str(input('Nome do primeiro aluno: ')).title()
a2 = str(input('Nome do Segundo aluno: ')).title()
a3 = str(input('Nome do Terceiro aluno: ')).title()
a4 = str(input('Nome do quarto aluno: ')).title()

nomes = (a1, a2, a3, a4)

print(f'A ordem de apresentação dos trabalhos será a seguinte: {sorted(nomes)}')
