#Faça um programa que leia uma frase pelo teclado e mostre na tela:
#-Quantas vezes aparece a letra 'a'
#-Em qual posição ela aparece pela primeira vez
#-Em que posição ela aparce por último.

frase = str(input('Digite uma frase: '))

print(f'A frase {frase.capitalize()}')
print(f'Tem {frase.upper().count("A")} letras "A"')
print(f'O "A" aparece pela primeira vez na posição {frase.upper().find("A")}')
print(f'O "A" aparece pela ultima vez na posição {frase.upper().rfind("A")}')
