from random import randint
from time import sleep
jogadores = {'Jogador 1':randint(1, 6), 'Jogador 2':randint(1, 6),
             'Jogador 3':randint(1, 6), 'Jogador 4':randint(1, 6)}
for j, n in jogadores.items():
    print(f'O {j} tirou {n} no dado.')
    sleep(1)
print('-=' * 15, f'\n{"RANKING DE JOGADORES":^30}')
print('-=' * 15)
pri = seg = ter = h = 0
jpri = jseg = jter = jqua = ''
for j, n in jogadores.items():
    if n >= pri:
        pri = n
        jpri = j
qua = pri
for j, n in jogadores.items():
    if n <= qua:
        qua = n
        jqua = j
del jogadores[jqua]
del jogadores[jpri]
for j, n in jogadores.items():
    if n >= seg:
        seg = n
        jseg = j
ter = seg
for j, n in jogadores.items():
    if n <= ter:
        ter = n
        jter = j
coloq = [jpri, jseg, jter, jqua]
for c in range(0, 4):
    sleep(1)
    print(f'{c + 1}º Lugar: {coloq[c]}')
