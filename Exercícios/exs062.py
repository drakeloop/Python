#Melhore o desafio exs061, perguntado para o usuário se ele quer mostrar mais alguns termos. O programa ecerra quando
#ele disser que quer mostrar 0 termos.

prim = int(input('Primeiro Termo: '))
raz = int(input('Razão: '))
mais = 10
ult = prim + (raz * mais)
cont = 0

while mais != 0:
    cont += mais
    while prim <= ult:
        print(prim, end='-->')
        prim += raz
    print('Pausa')
    mais = int(input('Deseja ver mais quantos termos: '))
    ult = prim + (raz * mais)
print(f'A progressão foi finalizada com {cont} termos mostrados.')
