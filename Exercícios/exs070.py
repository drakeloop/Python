#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário quer continuar
#ou não. No final mostre: -O valor total da compra, -Quantos produtos custam mais de R$1000.00, -Qual é o nome do
#produto mais barato.
linha = '-=' * 20
total = mmil = mbarato = qnt = 0
nbarato = ' '

print(f'{linha}\nLOJA GASTO MENOS')
while True:
    print(linha)
    nome = str(input('Nome do produto: '))
    valor = int(input('Preço: R$'))
    total += valor
    qnt += 1
    if valor > 1000:
        mmil += 1
    if qnt == 1:
        mbarato = valor
        nbarato = nome
    if qnt > 1:
        if valor < mbarato:
            mbarato = valor
            nbarato = nome

    seguir = ' '
    while seguir not in 'SN':
        seguir = str(input('Continuar comprando?[S/N]: ')).strip().upper()[0]
    if seguir == 'N':
        break
print(f'{linha}\n-->-->-->Compras Finalizadas\n{linha}')
print(f'Valor Total da compra: R${total:.2f}')
print(f'Produtos Acima de Mil reais: {mmil}')
print(f'Produto mais barato: {nbarato} de R${mbarato:.2f}')
