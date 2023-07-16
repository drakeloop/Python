#Crie um programa que leia uma frase qualquer e diga se ela é um polídromo ou não, desconsiderando os espaços.

frase = str(input('Digite uma palavra ou frase curta: ')).strip().upper()
inver = frase[::-1]

if inver == frase:
    print(f'Correto a frase/palavra {inver} é um polídromo.')
else:
    print(f'Não, a frase/palavra {frase} não é um polídromo.')
