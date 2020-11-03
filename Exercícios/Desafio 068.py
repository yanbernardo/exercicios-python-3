from random import randint
from time import sleep
cont = 0
while True:
    n_pc = randint(0,10)
    opcao = str(input('\033[1;30;107mEscolha \033[1;32;107mPar\033[1;30;107m ou\033[1;32;107m Ímpar\033[1;30;107m [P/I]:\033[m\n'))[0].upper()
    n_p = int(input('\033[1;30;107mDigite um número entre 0 e 10:\033[m\n'))
    print('\033[1;30;107mO computador escolheu\033[1;32;107m {}\033[m'.format(n_pc))
    if (n_pc + n_p) % 2 == 0:
        print('\033[1;31;107mPAR\033[m')
        jogo = 'P'
    else:
        jogo = 'I'
        print('\033[1;31;107mÍMPAR\033[m')
    if opcao == 'P' and jogo == 'P' or opcao == 'I' and jogo == 'I':
        print('\033[1;30;107mVOCÊ \033[1;32;107mGANHOU\033[1;30;107m!!\033[m')
        cont += 1
        print('\033[1;30;107mReiniciando...\033[m')
        sleep(1)
    else:
        break
print(f'\033[1;30;107mVocê perdeu após {cont} rodadas\033[m')
