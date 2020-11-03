tot = []
jogador = {}
gols = []
#Info do jogador
while True:
    jogador['nome'] = str(input('Nome do Jogador: ')).title()
    partidas = int(input('Partidas jogadas: '))
    for c in range(0, partidas):
        gols.append(int(input(f'Quantos gols marcados na {c+1}º partida?: ')))
    jogador['gols'] = gols[:]
    print('='*40)
#Calculo de gols no total
    jogador['total'] = 0
    for i in gols:
        jogador['total'] += i
    tot.append(jogador.copy())
    gols.clear()
#Saindo recursividade
    r = str(input('Deseja continuar?(S/N): ')).title()[0]
    if r in 'N':
        break
#Mostrando tudo
print('=-'*22)
print(f'{"Nome":<10}', f'{"Gols":^10}', f'{"Total":>20}')
print('=-'*22)
for jogador in tot:
    print(f'{jogador["nome"]:<12}', end=' ')
    print(f'{str(jogador["gols"]):<12}', end=' ')
    print(f'{jogador["total"]:>12}', end=' ')
    print()
print('=-'*22)
#Partidas e quantidade de gols
while True:
    name = str(input('Deseja ver informações sobre qual jogador?[Digite STOP para interromper]:\n')).title()
    if 'Stop' in name:
        break
    for jogador in tot:
        if jogador["nome"] == name:
            print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas')
            for c, p in enumerate(jogador['gols']):
                print(f'    ==>Na partida {c+1}, fez {p} gols')
            print(f'O Jogador {jogador["nome"]} fez um total de {jogador["total"]} gols!')
print('=-'*15)
print(f'{"VOLTE SEMPRE!":=^30}')
print('=-'*15)