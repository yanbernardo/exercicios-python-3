def leiaDinheiro(f):
    while True:
        n = str(input(f)).strip().replace(',', '.')
        try:
            return float(n)
        except:
            print(f'\033[1;31mERRO! "{n}" não é uma quanti válida.\033[m')


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
