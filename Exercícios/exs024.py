#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com a palavra 'santo'.

cidade = str(input('Digite o nome de uma cidade: ')).title()

print(f'A cidade {cidade}, começa com a palavra Santo: {"Santo" in cidade[:5]}')
