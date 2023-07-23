#Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de 0 até 20. Seu programa
#deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze',
           'Treze', 'Quartoze', 'Quinze', 'Dezesseis', 'Dezesete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if num >= 0 and num <= 20:
        break
print(f'O número {num}, escrito por extenso é {extenso[num]}.')
