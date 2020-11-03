while True:
    n = int(input('\033[1;30;107mDigite um número para ver sua tabuada\033[m\n\033[1;31;107m[DIGITE UM NÚMERO NEGATIVO PARA PARAR]\033[m\n'))
    if n < 0:
        break
    print('\033[1;30;107mTABUADA DE {}\033[m'.format(n))
    for c in range(1, 11):
        print('\033[1;30;107m{} x {} =\033[1;32m {}\033[m'.format(n, c, n*c))
print('\033[1;30;107mFim de EXECUÇÃO\033[m')
