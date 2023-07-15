#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule o IMC e mostre seu status, de acordo com os
#critérios determinados: -Abaixo de 18.5: Abaixo do peso, - Entre 18.5 e 25: Peso ideal, -Entre 25 e 30: Sobrepeso,
#-Entre 30 e 40: Obesidade e -Acima de 40: Obesidade Móbida.

print('Vamos averigar seu Indíce de Massa Corporal:')
peso = float(input('Peso ex(70.6): '))
alt = float(input('Altura ex(1.70): '))
imc = peso/(alt**2)

if imc < 18.5:
    print(f'Seu IMC é de {imc:.2f} Você está ABAIXO do peso recomendado.')
elif imc >= 18.5 and imc < 25:
    print(f'Seu IMC é de {imc:.2f} Você está no peso IDEAL para sua estatura.')
elif imc >= 25 and imc < 30:
    print(f'Seu IMC é de {imc:.2f} Você está com um SOBREPESO em relação a sua estatura')
elif imc >= 30 and imc < 40:
    print(f'Seu IMC é de {imc:.2f} Você está com OBESIDADE em relação a sua estatura')
elif imc >= 40:
    print(f'Seu IMC é de {imc:.2f} Você está com OBESIDADE MÓBIDA em relação a sua estatura')
