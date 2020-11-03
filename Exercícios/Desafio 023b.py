ret = 's'
while ret == 's' or ret == 'S':
    n = str(input('Digite um número de 0 a 9999:\n'))
    print('-' * 40)
    print('O número digitado foi:\n{}'.format(n))
    print('-' * 40)
    a = len(n)
    if a == 4:
        print('Unidade: {}'.format(n[3]))
        print('Dezena: {}'.format(n[2]))
        print('Centena: {}'.format(n[1]))
        print('Milhar: {}'.format(n[0]))
    if a == 3:
        print('Unidade: {}'.format(n[2]))
        print('Dezena: {}'.format(n[1]))
        print('Centena: {}'.format(n[0]))
    if a == 2:
        print('Unidade: {}'.format(n[1]))
        print('Dezena: {}'.format(n[0]))
    if a == 1:
        print('Unidade: {}'.format(n[0]))
    print('-' * 40)
    ret = input('Deseja continuar?(s/n)\n')
    print('-' * 40)
