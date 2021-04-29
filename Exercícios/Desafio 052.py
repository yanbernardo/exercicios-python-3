from time import sleep
while True:
    print('-='*15)
    print('CALCULADORA DE NÚMEROS PRIMOS')
    print('-='*15)
    n = int(input('Digite um número INTEIRO:\n'))
    conta = n
    vezes = 0
    for c in range(conta, 0, -1):
        if n % conta == 0:
            vezes += 1
            conta += -1
        else:
            conta += -1
    if vezes == 2:
        print('O número {} é PRIMO'.format(n))
    else:
        print('O numero {} NÃO é PRIMO'.format(n))
    rs = input('Deseja executar novamente? (tecle N para parar):\n')
    if rs in ['N', 'n']:
        print('Tecla N apertada, finalizando...')
        sleep(2)
        print('Fim de Execução.')
        break 
