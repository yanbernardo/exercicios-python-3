def leiaFloat(frase):
    while True:
        try:
            n = float(input(frase))
        except KeyboardInterrupt:
            print('O usuário preferiu não digitar este valor...')
            return 0
        except:
            print('\033[1;31mERRO! O item digitado não é um Número Real válido...\033[m')
        else:
            return n


def leiaInt(frase):
    while True:
        try:
            n = int(input(frase))
        except KeyboardInterrupt:
            print('O usuário preferiu não digitar este valor...')
            return 0
        except:
            print('\033[1;31mERRO! O item digitado não é um Número Inteiro válido...\033[m')
        else:
            return n


f = leiaFloat('Float: ')
i = leiaInt('Int: ')
print(f'O valor real foi {f} e o inteiro foi {i}')