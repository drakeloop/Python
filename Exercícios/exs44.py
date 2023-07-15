#Elabore um proograma que calcule o valor a ser pago por um produto considerando o seu preço nominal e a forma de
#pagamento: -À vista dinheiro/cheque: 10% de desconto, -À vista no Cartão: 5% de desconto, -Parcelado Em até 2X no
#cartão: preço normal, -Parcelado em 3X ou mais no catão: 20% de juros.

valor = float(input('Preço do Produto: R$'))
pag = int(input('[ 1 ] À vista: Dinheiro/Cheque '
                '\n[ 2 ] À vista: Crédito '
                '\n[ 3 ] Parcelado em 2X '
                '\n[ 4 ] Parcelado em 3X ou mais'
                '\nForma de pagamento: '))

if pag == 1:
    print(f'Dada a forma de pagamento terá um desconto de 10% o produto sairá por R${valor*0.9:.2f}')
elif pag == 2:
    print(f'Dada a forma de pagamento terá um desconto de 5% o produto sairá por R${valor * 0.95:.2f}')
elif pag == 3:
    print(f'Dada a forma de pagamento não terá desconto, produto sairá por R${valor:.2f}')
elif pag == 4:
    print(f'Dada a forma de pagamento terá um juros de 20% o produto sairá por R${valor * 1.2:.2f}')
    