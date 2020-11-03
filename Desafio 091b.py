from random import randint
from time import sleep
from operator import itemgetter
print('-='*16)
print(f'{"JOGO DE DADOS":-^31}')
print('-='*16)
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
ranking = list()
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-='*19)
print(f'{"RANKING":-^37}')
print('-='*19)
for i, v in enumerate(ranking):
    print(f'  ==>  {i + 1}º Lugar: {v[0]} com {v[1]} pontos')
    sleep(1)
print('-='*19)