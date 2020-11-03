while True:
    n_50 = n_20 = n_10 = n_1 = 0
    while True:
        try:
            value = int(input('Quanto deseja sacar?: R$'))
            break
        except ValueError:
            print('Somente números inteiros, Por Favor!!')
        print('Voce Recebeu:')
    while value >= 50:
        n_50 += 1
        value -= 50
    if n_50 > 0:
        print(f'{n_50} notas de 50 Reais')
    while value >= 20:
        n_20 += 1
        value -= 20
    if n_20 > 0:
        print(f'{n_20} notas de 20 Reais')
    while value >= 10:
        n_10 += 1
        value -= 10
    if n_10 > 0:
        print(f'{n_10} notas de 10 Reais')
    while value >= 1:
        n_1 += 1
        value -= 1
    if n_1 > 0:
        print(f'{n_1} notas de 1 Real')
    rst = str(input('Deseja continuar?[S/N}: ')).upper()[0]
    if rst == 'N':
        break
print('Fim de Execução!')
