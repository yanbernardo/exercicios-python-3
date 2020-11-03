print('\033[1;30;107m{}\033[m'.format('-='*10))
print('\033[1;30;107m{:-^20}\033[m'.format('Calculadora'))
print('\033[1;30;107m{}\033[m'.format('-='*10))
opcao = ''
while opcao != 5:
    n1 = float(input('\033[1;34;107mDigite um número:\033[m '))
    n2 = float(input('\033[1;34;107mDigite outro número:\033[m '))
    print('''\n\033[1;30;107mVocê deve selecionar uma operação:\033[m
    \033[1;32;107m[ 1 ] \033[1;34;107mSomar\033[m
    \033[1;32;107m[ 2 ] \033[1;34;107mMultiplicar\033[m
    \033[1;32;107m[ 3 ] \033[1;34;107mComparar\033[m
    \033[1;32;107m[ 4 ] \033[1;34;107mDigitar novos números\033[m
    \033[1;32;107m[ 5 ] \033[1;34;107mSair do programa\033[m''')
    opcao = int(input(''))

    if opcao != 5:
        if opcao == 1:
            print('\033[1;30;107mSomando...\033[m\n\033[1;32;107m{} + {} = {}\033[m'.format(n1, n2, n1 + n2))
        if opcao == 2:
            print('\033[1;30;107mMultiplicando...\033[m\n\033[1;32;107m{} x {} = {}\033[m'.format(n1, n2, n1 * n2))
        if opcao == 3:
            if n1 > n2:
                max = n1
                min = n2
            elif n2 > n1:
                min = n1
                max = n2
            elif n1 == n2:
                print('\033[1;30;107mComparando...\033[m\nOs valores {} e {} são iguais'.format(n1, n2))
            print('\033[1;30;107mComparando...\033[m\n\033[1;32;107mMAIOR: {}\033[m\n\033[1;32;107mMENOR: {}\033[m'.format(max, min))
        opcao = int(input('''\033[1;30;107mVocê deve selecionar uma opção:\033[m\n\033[1;32;107m[ 4 ] \033[1;34;107mDigitar novos números\033[m\n\033[1;32;107m[ 5 ] \033[1;34;107mSair do programa\033[m\n '''))
        if opcao == 4:
            print('\033[1;30;107m{:=^14}\033[m'.format('='))
            print('\033[1;30;107m{:=^10}\033[m'.format('REINICIANDO...'))
            print('\033[1;30;107m{:=^14}\033[m'.format('='))
    if opcao == 5:
        print('\033[1;30;107mFIM DE EXECUÇÃO\033[m')
