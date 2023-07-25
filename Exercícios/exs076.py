#Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na seqência. No final
#mostre uma listagem de preços organizando os dados em forma tabular.

lista = ('Mil Blocos', 890, '1m³ Areia', 160, '1m³ Pedra', 175, 'Saco de Cimento', 34, 'Metro do ferro', 28,
         'Caixa d´água', 760, 'Canduite 50 metros', 70)
linha = '--' * 25
print(f'{linha}\n              Listagem de Preços\n{linha}')
for pos, item in enumerate(lista):
    if pos % 2 == 0:
        print(f'{item:.<40}', end='')
    if pos % 2 > 0:
        print(f'R${item:7.2f}')
print(linha)
