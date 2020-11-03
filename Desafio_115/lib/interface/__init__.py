def lin():
    lin = '-' * 42
    return lin


def cabecalho(msg):
    msg = f'{msg:^42}'
    print(lin())
    print(msg.upper())
    print(lin())


def menu(lista):
    cabecalho('menu principal')
    for c, v in enumerate(lista):
        print(f'\033[1;32m{c + 1}\033[m - \033[1;34m{v}\033[m')
    print(lin())
    resp = leiaInt('\033[1;32mSua Opção:\033[m ')
    return resp


def leiaFloat(frase):
    while True:
        try:
            n = float(input(frase))
        except:
            print('\033[1;31mERRO! O item digitado não é um Número Real válido...\033[m')
        else:
            return n


def leiaInt(frase):
    while True:
        try:
            n = int(input(frase))
        except:
            print('\033[1;31mERRO! O item digitado não é um Número Inteiro válido...\033[m')
        else:
            return n

