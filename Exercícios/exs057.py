#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso errado, peça para ser
#digitado novamente.

sexo = str(input('Sexo [M/F]: ')).upper().strip()

while sexo not in 'MF':
    sexo = str(input('Resposta invalída. Informe seu Sexo [M/F]: ')).upper().strip()
print(f'Sexo {sexo} registrado com sucesso.')