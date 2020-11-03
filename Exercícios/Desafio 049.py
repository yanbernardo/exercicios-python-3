###PROGRAMA FEITO POR YAN BERNARDO###
rep = 's'
while rep == 's' or rep == 'S':
    n = int(input('\033[1;30;107mDigite um número para ver sua tabuada\033[m\n'))
    print('\033[1;30;107mTABUADA DE {}\033[m'.format(n))
    for c in range(1, 11):
        print('\033[1;30;107m{} x {} =\033[1;32m {}\033[m'.format(n, c, n*c))
    rep = input('\033[1;30;107mNova Tabuada? \033[1;32m(S/N)\033[m\n')
print('\033[1;30;107mPROGRAMA FEITO POR\033[1;32m YAN BERNARDO\033[m')
print('\033[1;32;107mFim de Execução...\033[m')