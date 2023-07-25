#Crie uma tupla preenchida pelos 20 primeiros colocados da tabela do Campeonato Brasileiro De Futebol, na Ordem de
#colocação, depois mostre: -Apenas os cinco primeiros colocados, -Os 4 ultimos colocados da tabela, -Uma lista com os
#times em ordem alfabética, -Em qual posição da tabela está o time do América.

brasileirao = ('.', 'Botafogo', 'Grêmio', 'Flamengo', 'Palmeiras', 'Atlético-PR', 'São Paulo', 'Fluminense', 'Bragantino',
               'Fortaleza', 'Internacional', 'Cruzeiro', 'Cuiabá', 'Atlético-MG', 'Santos', 'Corinthians', 'Goiás',
               'Bahia', 'Coritiba', 'América-MG', 'Vasco')
print(f'Os Cinco primeiros colocados são: {brasileirao[1:6]}')
print(f'Os quatros Ultimos São: {brasileirao[-4:]}')
print(f'Os times em Ordem alfabética: \n{sorted(brasileirao)}')
print(f'E o Bragantino está na posição {brasileirao.index("Bragantino")}')
