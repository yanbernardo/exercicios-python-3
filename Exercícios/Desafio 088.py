from random import randint
from time import sleep
jogos = list()
print('-+' * 20)
print('{:^40}'.format('MEGA-SENA DA VIRADA'))
print('-+' * 20)
qt = int(input('Deseja quantos jogos?: '))
for cont in range(0, qt):
    jogos.append(list())
    random = randint(1, 60)
    for c in range(0, 6):
        while random in jogos[cont]:
            random = randint(1, 60)
        else:
            jogos[cont].append(random)
    jogos[cont].sort()
    print(f'{cont + 1}º Jogo: {jogos[cont]}')
    sleep(0.5)
print('-+' * 20)
print('{:^40}'.format('BOA SORTE!'))
print('-+' * 20)
