def leiaInt(n):
    erro = 0
    f = n
    n = str(input(n))
    for c in n:
        if c not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-']:
            erro += 1
    if erro != 0 or len(n) == 0 or len(n) == 1 and n == '-' or '-' in n and '-' not in n[0] or '-' in n and '-' in n[1:]:
        print('\033[1;31mERRO! Digite um número inteiro válido.\033[m')
        return leiaInt(f)
    elif erro == 0:
        return int(n)


# Programa Principal
n = leiaInt('Digite um número: ')
print(f'Voce acabou de digitar o número {n}')
