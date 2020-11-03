n1 = int(input('\033[1;33;107mDigite um número inteiro para conversão\033[m\n'))
escolha = int(input("""\033[1;33;107mEscolha o grupo para qual deseja converter\033[m
\033[1;33;107m[ 1 ] Binário\033[m
\033[1;33;107m[ 2 ] Octal\033[m
\033[1;33;107m[ 3 ] Hexadecimal\033[m
\033[1;33;107mEscolha e pressione ENTER\033[m\n"""))
if escolha == 1:
    print('\033[1;33;107m{} convertido para BINÁRIO é igual a {}\033[m'.format(n1, bin(n1)[2:]))
elif escolha == 2:
    print('\033[1;33;107m{} convertido para OCTAL é igual a {}\033[m'.format(n1, oct(n1)[2:]))
elif escolha == 3:
    print('\033[1;33;107m{} convertido para HEXADECIMAL é igual a {}\033[m'.format(n1, hex(n1)[2:]))
else:
    print('\033[1;33;107mOpção inválida! Tente novamente\033[m')