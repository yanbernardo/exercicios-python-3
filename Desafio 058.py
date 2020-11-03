from random import randint
from time import sleep
nu = -2
nr = randint(0, 10)
palpite = 0
while nr != nu:
    nu = int(input('\n\033[1;30;107mAdvinhe o número que estou pensando entre 0 e 10:\033[m\n'))
    palpite += 1
    if nu < nr:
        print('\033[1;30;107mUm pouco \033[1;32;107mmais\033[1;30;107m...\033[m')
    elif nu > nr:
        print('\033[1;30;107mUm pouco \033[1;32;107mmenos\033[1;30;107m...\033[m')
print('\033[1;32;107mNossa, como você advinhou? Você é bom nisso!!\033[m')
print('\033[1;30;107mVocê adivinhou em \033[1;32;107m{}\033[1;30;107m palpites\033[m'.format(palpite))
print('\033[1;32;107mParabéns!!\033[m')
print('\033[1;97;107m-------------\033[m\n\033[1;30mFim de Jogo\033[m\n\033[1;97;107m-------------\033[m')