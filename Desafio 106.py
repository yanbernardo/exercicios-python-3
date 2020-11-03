from time import sleep


def titulo(titulo, cor='\033[m'):
    print(f'{cor}', end='')
    print('~' * (len(titulo) + 6))
    print(f'   {titulo}    ')
    print('~' * (len(titulo) + 6))
    print('\033[m')
    sleep(1)


cor = {'pad': '\033[m', 'lar': '\033[1;33m', 'verm': '\033[1;31;107m',
       'azul': '\033[1;34m', 'verd': '\033[1;32m', 'peb': '\033[1;30;107m',
       'bep': '\033[1;7;30;107m', 'aeb': '\033[1;7;34;40m'
       }

while True:
    titulo(f'SISTEMA DE AJUDA PyHELP', cor=cor['aeb'])
    ajuda = str(input('Função ou Biblioteca > ')).lower()
    if ajuda == 'fim':
        break
    else:
        titulo('Acessando a Biblioteca do Python...', cor=cor['peb'])
        sleep(3)
        print('\033[1;7;30;107m')
        help(ajuda)
        print('\033[m')
titulo('FIM DE EXECUÇÃO', cor=cor['verm'])


