def ficha(nome='<desconhecido>', gols=0):
    if len(nome) == 0:
        nome = '<desconhecido>'
    if gols == '':
        gols = 0
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


nome = str(input('Nome do Jogador: ')).capitalize()
gols = str(input('Gols no campeonato: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    ficha(gols=gols)
else:
    ficha(nome, gols)
