n_exec = 's'
while n_exec == 'S' or n_exec == 's':
    from random import randint
    nr = randint(0, 5)
    nu = int(input('\n Advinhe o número que estou pensando entre 0 e 5:\n'))
    if nu == nr:
        print('Nossa, como você advinhou? Você é bom nisso!!')
        print('Parabéns!!')
    else:
        print('Você errou, eu pensei no número {}'.format(nr))
        print('Boa sorte na proxima!!')
    n_exec = input('Deseja jogar novamente?(S/N)\n')
print('Foi um prazer jogar com você!!')