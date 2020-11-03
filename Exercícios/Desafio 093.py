jogador = dict()
gols = list()
#Nome e numero de partidas
jogador['nome'] = str(input('Nome do Jogador: ')).title()
partidas = int(input('Partidas jogadas: '))
#Gols por partida
for c in range(0, partidas):
    gols.append(int(input(f'Quantos gols marcados na {c+1}º partida?: ')))
jogador['gols'] = gols[:]
#Calculando o total de gols
jogador['total'] = sum(gols)
#Mostrando o dicionário
print('='*40)
print(jogador)
print('='*40)
#Mostrando as chaves e os valores
for slot, valor in jogador.items():
    print(f'O campo {slot} tem valor {valor}.')
print('='*40)
#Mostrando partidas e gols
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas')
for c, p in enumerate(jogador['gols']):
    print(f'    ==>Na partida {c+1}, fez {p} gols')
print(f'Foi um total de {jogador["total"]} gols!')
