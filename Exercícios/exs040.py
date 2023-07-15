#Crie um programna que leia duas notas de um aluno e calcule a sua média, mostrando uma mensagem no final, de acordo com
#a média atingida: -Média abaixo de 5.0: Reprovado, -Média entre 5.0 e 6.9: Recuperação, -Média 7.0 ou superior: Aprovado.

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda mota: '))
media = (n1+n2)/2

if media < 5:
    print(f'Você teve uma média de {media} e foi Reprovado.')
elif media >= 5 and media < 7:
    print(f'Você alcançou uma média de {media} e está de Recuperação.')
elif media >= 7:
    print(f'Você obteve uma média de {media} e está Aprovado.')
